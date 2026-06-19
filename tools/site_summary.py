def main():
    # 站点资料结构化数据集
    sites = [
        {
            "name": "爱游戏官方主站",
            "url": "https://mainsite-i-game.com.cn",
            "keywords": ["爱游戏", "游戏平台", "官方站点"],
            "tags": ["游戏", "门户", "综合"],
            "description": "爱游戏综合服务平台，提供游戏资讯、下载、社区互动等一站式服务。"
        },
        {
            "name": "爱游戏帮助中心",
            "url": "https://mainsite-i-game.com.cn/help",
            "keywords": ["爱游戏帮助", "客服", "FAQ"],
            "tags": ["客服", "帮助", "指南"],
            "description": "为用户提供常见问题解答、账号申诉、充值等帮助信息。"
        },
        {
            "name": "爱游戏论坛",
            "url": "https://mainsite-i-game.com.cn/community",
            "keywords": ["爱游戏社区", "论坛", "玩家交流"],
            "tags": ["社区", "交流", "玩家"],
            "description": "玩家交流讨论区，分享攻略、心得与活动资讯。"
        }
    ]

    print("=" * 60)
    print("          站点结构化摘要报告")
    print("=" * 60)

    for idx, site in enumerate(sites, start=1):
        print(f"\n【站点 {idx}】")
        print(f"  名称      : {site['name']}")
        print(f"  URL       : {site['url']}")
        print(f"  关键词    : {', '.join(site['keywords'])}")
        print(f"  标签      : {', '.join(site['tags'])}")
        print(f"  简要说明  : {site['description']}")

    print("\n" + "=" * 60)
    print("  摘要输出完成")
    print("=" * 60)


def generate_summary(data_list):
    lines = []
    for item in data_list:
        line = (
            f"[{item.get('name', '未命名')}] "
            f"URL: {item.get('url', '无')} | "
            f"关键词: {', '.join(item.get('keywords', []))} | "
            f"标签: {', '.join(item.get('tags', []))} | "
            f"简介: {item.get('description', '无')}"
        )
        lines.append(line)
    return "\n".join(lines)


def demo_usage():
    sample_data = [
        {
            "name": "爱游戏攻略站",
            "url": "https://mainsite-i-game.com.cn/guides",
            "keywords": ["爱游戏攻略", "教程", "秘籍"],
            "tags": ["攻略", "教程", "玩法"],
            "description": "聚合各类热门游戏攻略与技巧，帮助玩家快速上手。"
        }
    ]
    result = generate_summary(sample_data)
    print("\n【演示：单站点摘要】")
    print(result)


if __name__ == "__main__":
    main()
    demo_usage()