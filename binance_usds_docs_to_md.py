# -*- coding: utf-8 -*-
"""
自动抓取 Binance 衍生品（U 本位 / 币本位 / 期权 / 统一账户 / 统一账户专业版 / 期权测试网）
中文文档并转换为 Markdown，目录结构尽量贴合左侧导航。

目录结构示例（U 本位合约）：
    U本位合约/
        基本信息.md
        行情接口/
            REST API/
                获取交易规则和交易对.md
                合约下架日期.md
                深度信息.md
                ...
        交易接口/
            REST API/
                账户成交历史(USER-DATA).md
                ...
        账户接口/
            REST API/
                账户配置(USER-DATA).md
                ...
            WebSocket API/
                账户信息V2(USER-DATA).md
        合约钱包闪兑/
            查询订单状态(USER_DATA).md
        经典统一账户接口/
            查询经典统一账户账户信息(USER-DATA).md
        常见问题.md
        错误代码.md

依赖：
    pip install requests beautifulsoup4 markdownify
"""

import os
import re
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as html2markdown

# ---- 配置区域 -------------------------------------------------------------

BASE_ROOT = "https://developers.binance.com"

# 顶层产品根路径 -> 中文目录名（就是左边这几大块）
PRODUCT_ROOTS: dict[str, str] = {
    "/docs/zh-CN/derivatives/usds-margined-futures/": "U本位合约",
    #"/docs/zh-CN/derivatives/coin-margined-futures/": "币本位合约",
    #"/docs/zh-CN/derivatives/options/": "期权",
    "/docs/zh-CN/derivatives/portfolio-margin/": "统一账户",
    "/docs/zh-CN/derivatives/portfolio-margin-pro/": "统一账户专业版",
    #"/docs/zh-CN/derivatives/options-demo-trading/": "期权测试网",
}

DOC_ROOT_PATHS = list(PRODUCT_ROOTS.keys())
START_URLS = [urljoin(BASE_ROOT, p) for p in DOC_ROOT_PATHS]

# 中间路径段 slug -> 中文目录名（大部分来自左侧导航标题）
SLUG_TO_CN: dict[str, str] = {
    # 通用
    "general-info": "基本信息",
    "websocket-api-general-info": "WebSocket API基本信息",
    "common-definition": "通用枚举定义",

    "market-data": "行情接口",
    "trade": "交易接口",
    "websocket-market-streams": "Websocket行情推送",
    "user-data-streams": "Websocket账户信息推送",
    "account": "账户接口",
    "convert": "合约钱包闪兑",
    "portfolio-margin-endpoints": "经典统一账户接口",
    "faq": "常见问题",
    "error-code": "错误代码",

    # REST / WS 层
    "rest-api": "REST API",
    "websocket-api": "WebSocket API",

    # 统一账户 / 专业版的一些特殊 slug
    "portfolio-margin-user-data-streams": "用户数据流",
    "portfolio-margin-user-data-stream": "用户数据流",
    "portfolio-margin-pro-user-data-stream": "Websocket账户信息推送",

    # 期权 / 期权测试网里常见的
    "mm-api": "做市商接口",
    "block-trade": "大宗交易",
}

# 输出根目录
OUTPUT_DIR = "binance_derivatives_zhCN_md"

# 是否只抓 REST API 文档（URL 中包含 /rest-api/）
ONLY_REST_API = False

# 抓取间隔，避免太凶猛（秒）
REQUEST_DELAY = 0.5 # 每个请求之间的间隔，单位秒

# 自定义 UA，文明抓站
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BinanceDocsToMD/1.0; +https://developers.binance.com/)",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",   # 中文优先
}


# ---- 工具函数 -------------------------------------------------------------


def in_scope(url: str) -> bool:
    """判断一个 URL 是否属于我们关注的文档树（6 大产品）"""
    parsed = urlparse(url)
    path = parsed.path
    return any(path.startswith(root) for root in DOC_ROOT_PATHS)


def sanitize_filename(name: str) -> str:
    """把中文标题转成安全的文件名（保留中文，去掉非法字符）"""
    name = (name or "").strip()
    # 去掉 Windows 不允许的字符
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    # 把空白压成单个空格
    name = re.sub(r"\s+", " ", name)
    # 太长就截断一点，避免极端情况
    if len(name) > 80:
        name = name[:80]
    return name or "untitled"


# ---- 核心逻辑 -------------------------------------------------------------


def fetch_html(session: requests.Session, url: str) -> str:
    """下载页面 HTML 文本"""
    resp = session.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    return resp.text


def extract_links(html: str) -> set[str]:
    """
    从页面中提取继续抓取的链接：
    只保留属于 6 大产品文档树的链接
    """
    soup = BeautifulSoup(html, "html.parser")
    links: set[str] = set()

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith("#"):
            continue

        # 绝对化 URL
        full_url = urljoin(BASE_ROOT, href)
        parsed = urlparse(full_url)

        # 去掉 query / fragment，方便去重
        clean = parsed._replace(query="", fragment="").geturl()

        # 限定在我们配置的文档树下
        if not in_scope(clean):
            continue

        # 只要 REST API 的话，再过滤一层
        if ONLY_REST_API and "/rest-api/" not in clean:
            continue

        links.add(clean)

    return links


def extract_page_title(html: str) -> str | None:
    """
    从 HTML 中提取页面标题（优先 main 区域里的第一个 <h1>）
    """
    soup = BeautifulSoup(html, "html.parser")
    node = soup.find("main") or soup.find(attrs={"role": "main"}) or soup.body or soup
    h1 = node.find("h1") if node else None
    if h1:
        title = h1.get_text(strip=True)
        return title or None
    return None


def html_to_markdown(html: str) -> str:
    """
    尽量只取正文区域：
    - 优先找 <main> 标签
    - 其次 role="main"
    - 再不行就整个 <body>
    然后用 markdownify 转为 Markdown
    """
    soup = BeautifulSoup(html, "html.parser")

    node = soup.find("main")
    if node is None:
        node = soup.find(attrs={"role": "main"})
    if node is None:
        node = soup.body or soup

    md = html2markdown(str(node), heading_style="ATX")
    return md


def url_to_filepath(url: str, output_dir: str, page_title: str | None) -> str:
    """
    根据文档 URL + 页面标题生成本地 .md 文件路径，尽量模拟左侧导航结构：

    例：
      https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information

    解析为：
      产品根: usds-margined-futures        -> U本位合约
      第一段: market-data                  -> 行情接口
      第二段: rest-api                     -> REST API
      叶子页: Exchange-Information + <h1> 获取交易规则和交易对

    最终文件：
      <output_dir>/U本位合约/行情接口/REST API/获取交易规则和交易对.md
    """
    parsed = urlparse(url)
    path = parsed.path

    product_root = None
    product_name = None

    for root, prod_zh in PRODUCT_ROOTS.items():
        if path.startswith(root):
            product_root = root
            product_name = prod_zh
            break

    # 理论上不会走到这里；兜底一下
    if product_root is None:
        product_name = "_其它"
        rel_path = path.lstrip("/")
    else:
        rel_path = path[len(product_root):].strip("/")

    segments = [seg for seg in rel_path.split("/") if seg]

    # 产品首页：直接放一个 index.md
    if not segments:
        dirs = [product_name]
        filename = "index.md"
    else:
        leaf_slug = segments[-1]
        cat_slugs = segments[:-1]

        dirs = [product_name]

        # 中间目录：用 SLUG_TO_CN 做映射
        for slug in cat_slugs:
            zh = SLUG_TO_CN.get(slug, slug)
            dirs.append(sanitize_filename(zh))

        # 叶子文件名：优先用 h1 中文标题，没有就用 slug
        leaf_name = sanitize_filename(page_title) if page_title else sanitize_filename(leaf_slug)
        filename = f"{leaf_name}.md"

    full_dir = os.path.join(output_dir, *dirs)
    os.makedirs(full_dir, exist_ok=True)
    return os.path.join(full_dir, filename)


def crawl_all_docs(output_dir: str = OUTPUT_DIR, delay: float = REQUEST_DELAY) -> None:
    """广度优先抓取整个文档树并保存为 Markdown 文件"""
    os.makedirs(output_dir, exist_ok=True)

    visited: set[str] = set()
    to_visit: set[str] = set(START_URLS)

    session = requests.Session()

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue

        visited.add(url)
        print(f"[FETCH] {url}")

        try:
            html = fetch_html(session, url)
        except Exception as e:
            print(f"  [ERROR] 请求失败：{e}")
            continue

        # 提前抽出中文标题
        try:
            page_title = extract_page_title(html)
        except Exception as e:
            print(f"  [WARN] 提取标题失败：{e}")
            page_title = None

        # 转 Markdown
        try:
            md = html_to_markdown(html)
        except Exception as e:
            print(f"  [ERROR] HTML 转 Markdown 失败：{e}")
            continue

        # 生成带目录结构的文件路径
        filepath = url_to_filepath(url, output_dir, page_title)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"<!-- Source: {url} -->\n\n")
                f.write(md)
            print(f"  [OK] 保存到: {filepath}")
        except Exception as e:
            print(f"  [ERROR] 写文件失败：{e}")

        # 解析页面里的下一批链接
        try:
            new_links = extract_links(html)
            for link in new_links:
                if link not in visited:
                    to_visit.add(link)
        except Exception as e:
            print(f"  [WARN] 提取链接失败：{e}")

        # 友好一点，别太快
        time.sleep(delay)

    print(f"\n完成，总共抓取页面数：{len(visited)}")
    print(f"Markdown 文件目录：{os.path.abspath(output_dir)}")


if __name__ == "__main__":
    crawl_all_docs()
