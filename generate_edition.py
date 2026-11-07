#!/usr/bin/env python3
"""Generate expanded ASEAN-Daily-2026-11-07.html with 20 stories."""

STORIES = [
    {
        "id": "selloff",
        "kicker_en": "Regional · MARKET EVENT",
        "kicker_zh": "区域 · 市场事件",
        "h2_en": "Asian stocks suffer sharpest selloff in months as AI bubble fears spread",
        "h2_zh": "AI泡沫忧虑蔓延，亚洲股市遭遇数月来最大跌幅",
        "date_en": "Event: 6 November 2026. Multiple market sources.",
        "date_zh": "事件：2026年11月6日。来源：多家市场报道。",
        "verified_en": """Asian equity markets saw their largest single-day losses in months on 6 November. South Korea's KOSPI fell 8.6% to 4,923, triggering a 20-minute trading halt. Japan's Nikkei 225 dropped about 6%. Taiwan's TAIEX fell more than 8%. The selloff followed a 5.52% decline on the Nasdaq Composite and a more than 12% drop in the Philadelphia Semiconductor Index overnight.</p><p>The Institute of International Finance reported emerging-market net portfolio outflows of US$33.8 billion in October — the largest monthly outflow since March. Equity outflows totalled US$31.7 billion, with emerging Asia accounting for US$28.7 billion. Taiwan alone saw US$31.8 billion in equity sales, the largest monthly figure in IIF records dating to 2000.</p><p>In Southeast Asia, the Straits Times Index in Singapore fell sharply at market open, weighed down by the three major banks. Indonesia's Jakarta Composite Index also declined. The Philippine peso, already under pressure, weakened further to near P64 per US dollar. Regional currencies faced broad selling pressure as risk appetite evaporated.""",
        "verified_zh": """11月6日亚洲股市遭遇数月来最大单日跌幅。韩国KOSPI指数暴跌8.6%至4,923点，触发20分钟临时停牌。日经225指数跌约6%，台湾加权指数跌逾8%。此前纳斯达克综合指数跌5.52%，费城半导体指数跌逾12%。</p><p>国际金融协会(IIF)报告显示，10月新兴市场净投资组合流出338亿美元，为3月以来最大月度流出。股票流出317亿美元，其中亚洲新兴市场占287亿美元。台湾单月股票抛售达318亿美元，创IIF自2000年有记录以来最高。</p><p>东南亚方面，新加坡海峡时报指数在开盘时大幅下跌，三大银行股承压。印尼雅加达综合指数同步下挫。菲律宾比索本已承压，进一步走弱至接近64比索兑1美元。区域货币面临广泛抛售压力。""",
        "analysis_en": "The selloff was triggered by a combination of AI valuation doubts, profit-taking after strong gains, and warnings from major bank CEOs about potential 10–20% equity declines. For ASEAN businesses, the immediate question is whether this capital flight extends to regional markets and currencies, or remains concentrated in the tech-heavy North Asian exchanges. The Straits Times Index's decline underscores how interconnected regional banking and trade-dependent economies are to global tech sentiment. Southeast Asian central banks may face a dual challenge: supporting currencies while maintaining growth-friendly monetary conditions.",
        "analysis_zh": "此轮抛售由AI估值疑虑、获利回吐及大行CEO关于股市可能下跌10-20%的警告共同触发。东盟企业需关注资本外流是否从北亚科技股蔓延至本区域市场和货币。海峡时报指数的下跌凸显了区域银行业和依赖贸易的经济体与全球科技情绪的紧密关联。东南亚央行可能面临双重挑战：在支撑货币的同时维持有利于增长的货币政策环境。",
        "unknowns_en": "Whether this is a correction or the start of a broader downturn depends on upcoming tech earnings, US Federal Reserve signals, and whether AI investment commitments hold. Watch Southeast Asian currency and bond-flow data in coming weeks.",
        "source_url": "https://www.thailand-business-news.com/news/339062-thailand-business-news-morning-briefing-7",
        "source_label": "Thailand Business News · IIF data · MoneyOval"
    },
    {
        "id": "dbs-q3",
        "kicker_en": "Singapore · NEW RELEASE",
        "kicker_zh": "新加坡 · 新公告",
        "h2_en": "DBS posts S$2.81 billion Q3 profit as trading income cools, declares nine-month record",
        "h2_zh": "星展银行第三季净利28.1亿新元，交易收入降温，前九月创纪录",
        "date_en": "Released 5 Nov 2026; Q3 and nine-month 2026. DBS Group Holdings, Singapore.",
        "date_zh": "2026年11月5日公布；第三季度及前九个月业绩。星展集团控股，新加坡。",
        "verified_en": """DBS Group, Singapore's largest bank by assets, reported third-quarter net profit of S$2.81 billion, down 5% year on year. Total income fell 1%. The decline was attributed to lower market trading income amid unfavourable equity market conditions. However, nine-month net profit reached a record S$8.82 billion, up 2% year on year, on total income of S$17.9 billion — also a new high. Fee income and treasury customer sales grew by double-digit percentages to new highs in the nine-month period, led by wealth management. DBS's share price declined at market open on 6 November, weighing on the broader Straits Times Index.""",
        "verified_zh": """星展集团——新加坡资产规模最大的银行——第三季净利为28.1亿新元，同比下降5%。总收入同比降1%，主要因股市波动导致交易收入减少。但前九个月净利创纪录达88.2亿新元，同比增2%；总收入179亿新元，亦创新高。前九个月手续费收入及资金营销业务均录得双位数增长，财富管理领涨。星展股价11月6日开盘下跌，拖累海峡时报指数。""",
        "analysis_en": "DBS's mixed quarter — weaker trading but record nine-month earnings — mirrors the tension across Asian banking: strong wealth and lending franchises are generating sustained income, but market-sensitive revenue streams are vulnerable to the kind of volatility seen in the AI-driven selloff. With all three Singapore banks now reporting, the sector picture is clear: wealth management is the growth engine, but NIM compression and volatile trading are headwinds. For ASEAN corporates, the banks' continued lending momentum suggests credit conditions remain supportive, even as equity markets wobble.",
        "analysis_zh": "星展的喜忧参半——交易走弱但前九月创纪录——折射亚洲银行业的张力：财富管理和信贷业务持续创收，但市场敏感型收入在AI驱动的抛售中暴露了脆弱性。三大银行已全部公布业绩，财富管理是增长引擎，但净息差收窄和交易波动构成逆风。对东盟企业而言，银行持续的信贷扩张显示融资环境仍然有利。",
        "unknowns_en": "Whether wealth management growth can offset trading headwinds in Q4 depends on market recovery. Watch DBS's full-year guidance update and dividend policy.",
        "source_url": "https://www.malaymail.com/news/singapore/2026/11/05/singapores-largest-bank-dbs-reports-5pc-drop-in-third-quarter-net-profit/242118",
        "source_label": "Malay Mail / Reuters · DBS Q3 results"
    },
    {
        "id": "ocbc-guidance",
        "kicker_en": "Singapore · NEW RELEASE",
        "kicker_zh": "新加坡 · 新公告",
        "h2_en": "OCBC raises 2026 loan growth guidance after Q3 beat",
        "h2_zh": "华侨银行第三季业绩超预期，上调2026年贷款增长指引",
        "date_en": "Released 7 Nov 2026. Reuters via The Manila Times. Singapore.",
        "date_zh": "2026年11月7日公布。路透社经马尼拉时报报道。新加坡。",
        "verified_en": """OCBC raised its 2026 loan growth guidance to low double digits, from high-single to low-double digits previously. The bank also guided for total income growth of at least mid-single digits, and lowered its credit-cost guidance to 15–20 basis points from 20–25 basis points. Q3 net profit of S$2.04 billion slightly beat the S$2.01 billion analyst consensus. Net interest income rose 4% on loan growth, though net interest margin fell 18 basis points. Banking wealth management income (excluding Great Eastern) rose 2% to a record S$1.12 billion. Nine-month net profit rose 10% to S$6.24 billion.""",
        "verified_zh": """华侨银行将2026年贷款增长指引上调至低两位数，此前为高单位数至低两位数。同时预计总收入至少实现中单位数增长，信贷成本指引从20-25个基点下调至15-20个基点。第三季净利20.4亿新元，略超分析师预期的20.1亿新元。净利息收入受贷款增长推动增长4%，但净息差下降18个基点。银行财富管理收入（不含大东方）增2%至创纪录的11.2亿新元。前九个月净利同比增10%至62.4亿新元。""",
        "analysis_en": "OCBC's guidance upgrade signals confidence in lending demand across Asia, driven by the region's wealth boom. However, trading income fell 10% and insurance income fell 37%, showing how non-banking units can drag on group results. The lower credit-cost guidance suggests the bank sees stable asset quality ahead. Compared with DBS's 5% profit decline and UOB's weaker-than-expected results, OCBC's upgrade stands out — raising the question of whether this reflects bank-specific factors or broader lending momentum.",
        "analysis_zh": "上调指引反映亚洲贷款需求及财富增长的信心。但交易收入降10%、保险收入降37%，显示非银行业务对集团业绩的拖累。信贷成本下调显示资产质量预期稳定。相比星展净利降5%及大华银行业绩逊于预期，华侨银行的上调尤为突出。",
        "unknowns_en": "The bank said it is monitoring the Middle East conflict, energy markets and conditions in Indonesia. Peers DBS and UOB reported weaker-than-expected profits, raising questions about whether OCBC's upgrade reflects bank-specific factors or broader lending momentum.",
        "source_url": "https://www.manilatimes.net/2026/11/07/business/foreign-business/singapores-ocbc-raises-2026-guidance/2464238",
        "source_label": "Manila Times / Reuters · OCBC raises 2026 guidance"
    },
    {
        "id": "uob-q3",
        "kicker_en": "Singapore · NEW RELEASE",
        "kicker_zh": "新加坡 · 新公告",
        "h2_en": "UOB Q3 profit misses forecasts as NIM compresses; wealth income hits record",
        "h2_zh": "大华银行第三季净利低于预期，净息差收窄；财富管理收入创新高",
        "date_en": "Released 4 Nov 2026; Q3 2026. United Overseas Bank, Singapore.",
        "date_zh": "2026年11月4日公布；第三季度业绩。大华银行，新加坡。",
        "verified_en": """UOB reported Q3 net profit of S$1.25 billion, missing the S$1.38 billion analyst consensus and falling 15% from the previous quarter. Net interest income was S$2.28 billion, down 1% quarter on quarter and up 1% year on year. Net interest margin declined to 1.68%, down 6 basis points from 1.74% in Q2. Net fee income hit a record S$733 million, up 10% quarter on quarter and 19% year on year, driven by wealth management and credit cards. Customer loans grew 3% quarter on quarter and 6% year on year to S$372 billion, with trade loans surging 31% year on year. The non-performing loan ratio improved to 1.5% from 1.6%. Nine-month net profit was S$4.17 billion, up 27% year on year. Credit costs were 24 basis points, within the 25–30 bps full-year guidance.""",
        "verified_zh": """大华银行第三季净利12.5亿新元，低于分析师预期的13.8亿新元，环比降15%。净利息收入22.8亿新元，环比降1%、同比增1%。净息差降至1.68%，环比下降6个基点。净手续费收入创纪录达7.33亿新元，环比增10%、同比增19%，财富管理和信用卡驱动增长。客户贷款环比增3%、同比增6%至3,720亿新元，贸易贷款同比猛增31%。不良贷款率从1.6%改善至1.5%。前九个月净利41.7亿新元，同比增27%。信贷成本24个基点，处于全年25-30个基点的指引范围内。""",
        "analysis_en": "UOB's quarter reveals the NIM compression hitting Singapore banks as funding costs catch up with lending rates. The 31% trade loan surge, however, signals strong cross-border trade financing demand — particularly relevant given ASEAN's robust intra-regional trade growth. The record fee income shows the wealth management pivot is working. Greater China NPL ratio at 5.0% (up from 4.8%) bears watching as a potential source of provisions. The bank's mid-single-digit 2027 loan growth guidance suggests cautious optimism about the lending environment ahead.",
        "analysis_zh": "大华银行本季反映出新加坡银行面临的净息差收窄压力。但贸易贷款猛增31%显示跨境贸易融资需求强劲——对东盟区内贸易增长尤为重要。创纪录的手续费收入说明财富管理转型见效。大中华区不良率升至5.0%需关注。2027年中单位数贷款增长指引显示对信贷环境的审慎乐观。",
        "unknowns_en": "Whether NIM stabilises in Q4 depends on deposit repricing dynamics. Greater China property exposure (NPL at 3.8% for real estate and hospitality) remains a risk to watch. No dividend was declared in Q3.",
        "source_url": "https://growbeansprout.com/uob-3q26-profit-dividend",
        "source_label": "Growbeansprout · UOB 3Q26 results analysis"
    },
    {
        "id": "mapletree-ipo",
        "kicker_en": "Singapore · CORPORATE",
        "kicker_zh": "新加坡 · 企业",
        "h2_en": "Temasek's Mapletree plans S$1 billion Singapore IPO for 2027",
        "h2_zh": "淡马锡旗下丰树投资计划2027年在新加坡上市，融资10亿新元",
        "date_en": "Reported 5–7 Nov 2026. Multiple financial media sources.",
        "date_zh": "2026年11月5-7日报道。多家财经媒体。",
        "verified_en": """Mapletree Investments, the property arm of Singapore sovereign fund Temasek Holdings, is planning a Singapore IPO that could raise about S$1 billion (approximately US$780 million), according to multiple media reports. Mapletree manages approximately US$59.5 billion in assets. The IPO is expected in 2027. The listing structure — whether a REIT or a broader holding company — was not specified in the reports. Mapletree already manages four listed REITs on the SGX. The company has been reported to be hiring banks for the offering.""",
        "verified_zh": """据多家媒体报道，淡马锡旗下房地产子公司丰树投资计划在新加坡进行首次公开募股，融资约10亿新元（约7.8亿美元）。丰树目前管理约595亿美元资产，预计2027年上市。报道未明确上市结构是REIT还是更广泛的控股公司。丰树已在新交所管理四只上市REIT。据报道公司正在聘请承销银行。""",
        "analysis_en": "If completed, this would be one of the largest Singapore IPOs in recent years and a significant vote of confidence in the SGX. The timing is notable — Mapletree is moving forward despite the current market turbulence, suggesting Temasek sees a window for real estate listings. The IPO could create the SGX's largest property-focused listing and draw international investor attention to Southeast Asian real estate valuations. For the region's property sector, it could also set a benchmark for other large private real estate portfolios considering public listings.",
        "analysis_zh": "若完成，这将是近年来新加坡最大的IPO之一，也是对新交所的重大信心投票。在当前市场动荡之际推进，显示淡马锡看到了房地产上市的窗口。该IPO可能创造新交所最大的房地产上市，并引导国际投资者关注东南亚房地产估值。",
        "unknowns_en": "The listing structure, exact timeline, and market conditions at the time of pricing are all uncertain. Whether the current equity market volatility delays the offering remains to be seen.",
        "source_url": "https://www.thestar.com.my/business/business-news/2026/11/05/temaseks-mapletree-picks-banks-for-singapore-ipo",
        "source_label": "The Star · Mapletree IPO report"
    },
    {
        "id": "sia-seats",
        "kicker_en": "Singapore · CORPORATE",
        "kicker_zh": "新加坡 · 企业",
        "h2_en": "Singapore Airlines unveils S$2 billion cabin overhaul, its largest ever",
        "h2_zh": "新加坡航空投入20亿新元全面更新客舱，为历来最大投资",
        "date_en": "Announced 6 Nov 2026. Singapore Airlines.",
        "date_zh": "2026年11月6日公布。新加坡航空。",
        "verified_en": """Singapore Airlines unveiled new seat products across all four cabin classes — its largest-ever investment at S$2 billion. The seats will go into retrofitted Airbus A350 aircraft and new Boeing 777-9s. First Class gets 1-2-1 suites with 80-inch beds and retractable centre dividers for double beds. Business Class features 1-2-1 seats with 79-inch flat beds and privacy doors. Premium Economy and Economy also receive new designs. Entry into service is expected H2 2027, with A350 retrofit completion targeted by end 2030. The investment underscores the airline's strategy of competing on premium product quality in Asia's growing long-haul market.""",
        "verified_zh": """新加坡航空发布四舱全新座椅产品，投资额达20亿新元，为历来最大。新座椅将安装于改装的A350机队及新波音777-9。头等舱采用1-2-1布局套间，配80英寸床及可收回隔板实现双人床。商务舱配79英寸全平躺床及隐私门。高级经济舱和经济舱也获全新设计。预计2027年下半年投入服务，A350改装目标于2030年底完成。该投资凸显新航在亚洲日益增长的远程市场中以高端产品竞争的战略。""",
        "analysis_en": "The investment signals SIA's bet on premium travel demand in Asia. However, the timeline carries execution risk: the Boeing 777-9 is certified but not yet in service, and the A350 seat certification is still pending. Competitors have been upgrading aggressively; whether SIA's new product arrives fast enough to maintain its premium positioning is the key question. The S$2 billion spend also comes at a time when the airline industry faces fuel-price uncertainty and potential headwinds from the global equity selloff dampening corporate travel budgets.",
        "analysis_zh": "巨额投资反映新航看好亚洲高端旅行需求。但时间线存在执行风险：777-9已获认证但尚未服役，A350座椅认证仍在进行中。竞争对手也在积极升级，新产品能否及时上线以维持高端定位是关键。20亿新元的支出正值航空业面临燃油价格不确定性及全球股市抛售可能抑制企业差旅预算之际。",
        "unknowns_en": "Boeing 777-9 delivery timeline remains uncertain. Watch for fare and yield impacts once the new cabins enter service.",
        "source_url": "https://milelion.com/2026/11/06/unveiled-singapore-airlines-new-first-business-premium-economy-and-economy-seats/",
        "source_label": "The MileLion · SIA cabin unveiling"
    },
    {
        "id": "google-my",
        "kicker_en": "Malaysia · INVESTMENT",
        "kicker_zh": "马来西亚 · 投资",
        "h2_en": "Google commits US$15 billion to Malaysia data centres, projecting 37,000 jobs",
        "h2_zh": "谷歌承诺向马来西亚数据中心投资150亿美元，预计创造3.7万个岗位",
        "date_en": "Announced 4 Nov 2026. Google official blog. Kuala Lumpur.",
        "date_zh": "2026年11月4日公布。谷歌官方博客。吉隆坡。",
        "verified_en": """Google announced a US$15 billion investment in Malaysia over 2027–2028, its largest commitment in the country. The investment will fund new data centre campuses in Selangor and Negeri Sembilan, building on Google's first operational data centre at Elmina Business Park. Google projected more than 37,000 local jobs per year during construction, with 6,000 in construction roles and average annual labour income of US$378 million. Operations would support more than 9,000 jobs per year at wages averaging 45% above the national median. The investment includes more than 1 GW of new clean energy capacity for Malaysia's national grid, a collaboration with Tenaga Nasional Berhad, and community water-replenishment projects in Selangor and Negeri Sembilan. Google also committed to upskilling approximately 800,000 Malaysians from 2027 to 2031 through AI literacy programmes. Ruth Porat, President and Chief Investment Officer of Alphabet, said Google is "committed to growing our presence responsibly." This follows Google's 2024 commitment of US$2 billion to Malaysia.""",
        "verified_zh": """谷歌宣布2027-2028年间向马来西亚投资150亿美元，为其在该国最大承诺。资金将用于在雪兰莪和森美兰建设新数据中心园区，建立在Elmina商业园首个运营数据中心的基础上。谷歌预计建设期每年创造逾37,000个本地岗位，其中6,000个为建筑岗位，年均劳动收入3.78亿美元。运营期每年支撑逾9,000个岗位，薪资平均高于全国中位数45%。投资还包括为马来西亚国家电网新增逾1吉瓦清洁能源产能，与国家能源公司合作，以及在雪兰莪和森美兰的水资源补充项目。谷歌还承诺2027-2031年为约80万马来西亚人提供AI技能培训。Alphabet总裁兼首席投资官Ruth Porat表示谷歌"致力于负责任地扩大在马来西亚的业务"。此前谷歌于2024年曾承诺在马来西亚投资20亿美元。""",
        "analysis_en": "Google's US$15 billion bet makes Malaysia one of the largest data-centre destinations in Southeast Asia and validates the country's positioning as an AI infrastructure hub. The scale dwarfs Google's 2024 commitment by 7.5 times. Combined with Microsoft's existing investments and other hyperscaler commitments, Malaysia is emerging as a serious alternative to Singapore for cloud and AI workloads — with lower land costs but potential power-supply challenges. The 1 GW clean-energy commitment is notable given concerns about data-centre energy demand straining national grids across the region. For Malaysian businesses, the downstream effects in construction, power, and digital skills could be transformative.",
        "analysis_zh": "谷歌150亿美元的投注使马来西亚成为东南亚最大的数据中心目的地之一，验证了该国作为AI基础设施枢纽的定位。规模是2024年承诺的7.5倍。加上微软等超大规模企业的现有投资，马来西亚正成为新加坡之外云计算和AI工作负载的有力替代——土地成本更低但可能面临电力供应挑战。1吉瓦清洁能源承诺值得关注，鉴于各方对数据中心能源需求给区域电网带来压力的担忧。对马来西亚企业而言，建筑、电力和数字技能方面的下游效应可能具有变革性。",
        "unknowns_en": "Whether power-grid capacity can keep pace with data-centre demand is a key uncertainty. The job projections are Google's own estimates and have not been independently verified. Watch electricity pricing and grid-reliability data as construction begins.",
        "source_url": "https://blog.google/intl/en-my/company-news/inside-google/google-investment-malaysia-digital-infrastructure-november-2026/",
        "source_label": "Google Official Blog · Malaysia investment announcement"
    },
    {
        "id": "my-tourism",
        "kicker_en": "Malaysia · TOURISM",
        "kicker_zh": "马来西亚 · 旅游",
        "h2_en": "Malaysia draws 32.3 million visitors in nine months, targets 43 million for 2026",
        "h2_zh": "马来西亚前九个月接待3,230万游客，2026年目标4,300万",
        "date_en": "Data: January–September 2026. Visit Malaysia 2026 campaign.",
        "date_zh": "数据：2026年1至9月。马来西亚旅游年活动。",
        "verified_en": """Malaysia recorded 32.3 million international arrivals in the first nine months of 2026, up 2.4% from 31.5 million in the same period of 2025. The Visit Malaysia 2026 target is 43 million visitors. Tourism contributed RM323 billion in value added in 2025, or 15.9% of GDP, supporting about 3.7 million jobs. In Kuala Lumpur, JLL projected 1,384 new hotel rooms in 2026, about 60% luxury. The Waldorf Astoria Kuala Lumpur opened in October with 268 suites. Langkawi expects about 1,750 additional upscale rooms within two years, raising five-star inventory by roughly 85%.""",
        "verified_zh": """2026年前九个月马来西亚接待国际旅客3,230万人次，同比增2.4%。旅游年目标为4,300万。2025年旅游业增加值达3,230亿令吉，占GDP的15.9%，支撑约370万个就业岗位。吉隆坡预计2026年新增1,384间酒店客房，约60%为豪华级。华尔道夫吉隆坡酒店10月开业，设268间套房。兰卡威未来两年预计新增约1,750间高端客房，五星级库存增长约85%。""",
        "analysis_en": "At 32.3 million arrivals through September, Malaysia needs about 10.7 million visitors in the final quarter to hit its 43-million target — achievable given seasonal peaks but ambitious. The luxury hotel pipeline suggests operators are betting on higher-spending visitors rather than just volume. Langkawi's 85% jump in five-star rooms is a particularly bold bet that could reshape the island's tourism economics. However, the 2.4% growth rate is significantly below the kind of momentum needed for a 'Visit Malaysia Year' to deliver transformative results.",
        "analysis_zh": "前九个月3,230万人次意味着第四季需再吸引约1,070万游客才能达标——有季节性旺季支撑但仍具挑战。豪华酒店供给大增显示业者看好高消费客群。兰卡威五星级客房增85%是大胆押注。但2.4%的增速远低于'旅游年'实现转型性成果所需的势头。",
        "unknowns_en": "Whether the luxury supply can be absorbed depends on airlift capacity and whether premium travellers shift from competitors like Thailand and Bali. Watch Q4 arrival figures and hotel occupancy rates.",
        "source_url": "https://www.travelandtourworld.com/news/article/1v8mxy4d1e8a/",
        "source_label": "Travel and Tour World · Malaysia tourism 2026"
    },
    {
        "id": "indo-gdp",
        "kicker_en": "Indonesia · NEW RELEASE",
        "kicker_zh": "印度尼西亚 · 新公告",
        "h2_en": "Indonesia's Q3 GDP grows 5.47%, beating forecasts on strong household spending",
        "h2_zh": "印尼第三季GDP增长5.47%，家庭支出强劲，超出预期",
        "date_en": "Released 5 Nov 2026; reference period Q3 2026. Jakarta.",
        "date_zh": "2026年11月5日公布；统计期为第三季度，雅加达。",
        "verified_en": """Indonesia's GDP grew 5.47% year on year in the third quarter, accelerating from 5.29% in Q2 and beating the 5.18% Reuters poll forecast. Quarter-on-quarter growth was 1.59%. Exports grew 4.59%, household consumption rose 5.04%, and government spending increased 8.95%. The government said it expects full-year growth of 5.4–5.5%. Indonesia's economy, the largest in Southeast Asia, continues to grow above the 5% threshold that policymakers consider necessary for meaningful job creation and poverty reduction.""",
        "verified_zh": """印尼第三季GDP同比增长5.47%，高于第二季的5.29%，超出路透调查预期的5.18%。环比增长1.59%。出口增4.59%，家庭消费增5.04%，政府支出增8.95%。政府预计全年增长5.4-5.5%。印尼作为东南亚最大经济体，继续保持在政策制定者认为创造就业和减贫所需的5%以上增速。""",
        "analysis_en": "Indonesia's growth beat comes at a time when many Asian economies face headwinds from the tech selloff and capital outflows. The strong government spending component raises questions about sustainability, while robust household consumption suggests resilient domestic demand. The 5.47% figure keeps Indonesia comfortably above the Philippines (2.3% Q2) and Thailand (around 2.4%), reinforcing its position as the ASEAN growth anchor. Businesses should assess whether the growth is broad-based or concentrated in specific sectors.",
        "analysis_zh": "在亚洲多国面临科技股抛售和资本外流之际，印尼经济超预期增长。政府支出贡献较大，可持续性有待观察；家庭消费强劲显示内需韧性。5.47%使印尼稳居菲律宾（第二季2.3%）和泰国（约2.4%）之上，巩固了其作为东盟增长支柱的地位。",
        "unknowns_en": "The composition of export growth by commodity and destination is not fully detailed. Watch whether the capital outflows hitting other Asian markets spill over to Indonesian assets and the rupiah.",
        "source_url": "https://www.thailand-business-news.com/news/339062-thailand-business-news-morning-briefing-7",
        "source_label": "Thailand Business News · Indonesia GDP data"
    },
    {
        "id": "indo-nickel",
        "kicker_en": "Indonesia · COMMODITIES",
        "kicker_zh": "印度尼西亚 · 大宗商品",
        "h2_en": "Indonesia targets US$45 billion in nickel downstream exports as industrial strategy deepens",
        "h2_zh": "印尼将镍下游出口目标提高至450亿美元，产业战略持续深化",
        "date_en": "Target set for 2026. Ministry of Energy and Mineral Resources, Jakarta.",
        "date_zh": "2026年出口目标。能源与矿产资源部，雅加达。",
        "verified_en": """Indonesia's Energy and Mineral Resources Ministry raised its 2026 nickel downstream export target to US$45 billion, up from approximately US$40 billion achieved in 2025. The target represents a 12.5% increase. Indonesia has banned raw nickel ore exports since 2020, forcing foreign and domestic investors to build smelters and processing plants domestically. The downstream strategy has produced stainless steel, ferronickel, nickel pig iron, and increasingly battery-grade nickel for the EV supply chain. Indonesia controls roughly half the world's nickel reserves and is the dominant global producer. The government is now studying whether to extend a similar export ban to tin, potentially affecting global supply of the metal used in electronics soldering and packaging.""",
        "verified_zh": """印尼能源与矿产资源部将2026年镍下游产品出口目标提高至450亿美元，2025年实现约400亿美元，增幅12.5%。印尼自2020年起禁止镍矿石原矿出口，迫使投资者在国内建设冶炼厂和加工厂。下游战略已生产不锈钢、镍铁、镍生铁，以及越来越多的电池级镍用于电动汽车供应链。印尼控制全球约半数镍储量，是全球主要生产国。政府正研究是否对锡实施类似出口禁令，可能影响电子焊接和封装用金属的全球供应。""",
        "analysis_en": "Indonesia's nickel downstreaming is arguably the most successful industrial policy in Southeast Asia this decade. Moving from raw ore exports to US$45 billion in processed products has created domestic jobs, attracted billions in smelter investment (particularly from China), and positioned Indonesia as the indispensable link in the global EV battery chain. The potential tin ban signals that Jakarta sees this model as replicable across its mineral wealth. For ASEAN businesses, the implications are twofold: supply-chain security for nickel-dependent industries, and a template that other resource-rich nations may follow.",
        "analysis_zh": "印尼的镍下游加工可能是本十年东南亚最成功的产业政策。从原矿出口到450亿美元加工产品，创造了国内就业，吸引了数十亿冶炼投资（尤其来自中国），并使印尼成为全球电动汽车电池链中不可或缺的环节。潜在的锡出口禁令表明雅加达认为这一模式可在其矿产资源中复制。对东盟企业有双重启示：镍依赖产业的供应链安全，以及其他资源丰富国家可能效仿的模板。",
        "unknowns_en": "Whether the US$45 billion target is achievable depends on global nickel prices, which have been volatile. The tin export ban is under study, not confirmed. Environmental concerns around nickel smelting in Sulawesi also remain unresolved.",
        "source_url": "https://en.vietnamplus.vn/indonesia-targets-at-least-45-bln-usd-in-nickel-exports-in-2026-post354566.vnp",
        "source_label": "VietnamPlus / Antara · Indonesia nickel target"
    },
    {
        "id": "indo-dc",
        "kicker_en": "Indonesia · INVESTMENT",
        "kicker_zh": "印度尼西亚 · 投资",
        "h2_en": "Digital Edge commits US$4.5 billion to build Indonesia's largest AI-ready data centre",
        "h2_zh": "Digital Edge斥资45亿美元建设印尼最大AI就绪数据中心",
        "date_en": "Announced January 2026; construction ongoing. Jakarta.",
        "date_zh": "2026年1月公布；建设进行中。雅加达。",
        "verified_en": """Digital Edge, a data centre platform backed by Stonepeak Partners, committed US$4.5 billion to build a 500-megawatt AI-ready hyperscale data centre campus in the Jakarta metropolitan area. The project is described as Indonesia's largest data centre and one of the largest in Southeast Asia. Digital Edge subsequently raised US$665 million in financing for the project. The campus is designed to support artificial intelligence workloads and cloud computing, targeting major hyperscale tenants. Indonesia's data centre market has been growing rapidly as the country's 280 million population and accelerating digital economy attract global infrastructure investors.""",
        "verified_zh": """由Stonepeak Partners支持的数据中心平台Digital Edge承诺投资45亿美元，在雅加达大都市区建设一座500兆瓦的AI就绪超大规模数据中心园区。该项目被描述为印尼最大的数据中心，也是东南亚最大的数据中心之一。Digital Edge随后为该项目融资6.65亿美元。该园区旨在支持人工智能工作负载和云计算，面向大型超大规模租户。印尼2.8亿人口和加速发展的数字经济正吸引全球基础设施投资者，数据中心市场快速增长。""",
        "analysis_en": "The US$4.5 billion commitment — combined with Google's US$15 billion for Malaysia — illustrates how Southeast Asia is becoming the frontier for global data-centre expansion, driven by AI demand and China-plus-one strategies. Indonesia's advantage is scale: 280 million consumers and a fast-growing digital economy make it the natural anchor market for the archipelago. The challenge is infrastructure — reliable power, connectivity, and cooling in a tropical climate. This investment could accelerate Indonesia's digital transformation but also raises questions about energy policy and grid capacity.",
        "analysis_zh": "45亿美元的承诺——加上谷歌对马来西亚的150亿美元——说明东南亚正成为全球数据中心扩张的前沿，由AI需求和中国+1战略驱动。印尼的优势在于规模：2.8亿消费者和快速增长的数字经济。挑战在于基础设施——热带气候下的可靠电力、连接和冷却。该投资可能加速印尼数字化转型，但也引发能源政策和电网容量问题。",
        "unknowns_en": "Construction timeline and occupancy ramp are not confirmed. Power sourcing for 500 MW of capacity in the Jakarta area will be critical. Whether this investment is confirmed at the current scale given the global AI valuation reset is worth watching.",
        "source_url": "https://pulse2.com/digital-edge-commits-4-5-billion-to-build-indonesias-largest-500mw-ai-ready-hyperscale-data-center-campus",
        "source_label": "Pulse2 · Digital Edge Indonesia data centre"
    },
    {
        "id": "gulf-energy",
        "kicker_en": "Thailand · CORPORATE",
        "kicker_zh": "泰国 · 企业",
        "h2_en": "Thailand's GULF Energy posts 28% profit jump on solar and data-centre expansion",
        "h2_zh": "泰国GULF能源净利增28%，太阳能与数据中心驱动增长",
        "date_en": "Q3 2026 results reported 6 Nov 2026. Gulf Energy Development (GULF).",
        "date_zh": "2026年第三季业绩，11月6日公布。Gulf Energy Development。",
        "verified_en": """Gulf Energy Development reported Q3 net profit attributable to shareholders of THB9.289 billion, up 28% year on year. Core profit rose 24% to THB9.045 billion. Revenue surged 75% to THB52.809 billion. The company maintained 2026 revenue and EBITDA growth guidance of 12–15%. Four solar and solar-plus-storage projects totalling 373 MW are expected to start in November and December. GULF now operates 14 domestic solar projects with 1,379 MW capacity, up from five projects totalling 532 MW a year earlier — a nearly threefold increase. Its digital business returned to profitability after its GSA01 data centre began full operation in June.""",
        "verified_zh": """GULF第三季归母净利92.89亿泰铢，同比增28%。核心净利90.45亿泰铢，增24%。营收528.09亿泰铢，猛增75%。公司维持2026年营收和EBITDA增长12-15%的指引。11至12月将有4个太阳能及储能项目共373MW投运。目前运营14个国内太阳能项目，装机1,379MW，较一年前5个项目532MW大幅增长——接近三倍。数据中心业务在GSA01于6月全面运营后恢复盈利。""",
        "analysis_en": "GULF's results highlight two major trends in Southeast Asian energy: the accelerating shift to solar power and the growing intersection of energy and data centres. The company's rapid solar expansion — from 532 MW to 1,379 MW in one year — reflects Thailand's aggressive renewable-energy push and GULF's positioning as an integrated energy-digital infrastructure player. The data-centre profitability milestone is notable given the broader AI infrastructure buildout across the region. Revenue surging 75% suggests the growth is not just organic but also includes newly consolidated assets or one-time items that warrant scrutiny.",
        "analysis_zh": "业绩凸显东南亚能源两大趋势——太阳能加速发展及能源与数据中心融合。一年内太阳能装机从532MW增至1,379MW，反映泰国激进的可再生能源政策和GULF作为综合能源-数字基础设施企业的定位。数据中心扭亏为盈值得关注。营收猛增75%暗示增长可能包含新纳入合并范围的资产或一次性项目。",
        "unknowns_en": "Whether GULF's revenue growth rate is sustainable at 75% depends on one-off contributions versus recurring operations. Watch the commissioning of the 373 MW in new solar capacity and whether data-centre profitability is maintained.",
        "source_url": "https://www.thailand-business-news.com/news/339062-thailand-business-news-morning-briefing-7",
        "source_label": "Thailand Business News · GULF Q3 results"
    },
    {
        "id": "bot-gdp",
        "kicker_en": "Thailand · ECONOMY",
        "kicker_zh": "泰国 · 经济",
        "h2_en": "Bank of Thailand revises 2026 growth forecast to 2.4%, sees potential for 2.9% with data update",
        "h2_zh": "泰国央行将2026年增长预测上调至2.4%，数据修订后或达2.9%",
        "date_en": "Reported 6 Nov 2026. Bank of Thailand governor remarks.",
        "date_zh": "2026年11月6日报道。泰国央行行长讲话。",
        "verified_en": """The Bank of Thailand raised its 2026 GDP growth forecast to 2.4%, up from 2.3% previously. Pending revisions to the Manufacturing Production Index could add 0.1 to 0.5 percentage points, potentially lifting headline growth to between 2.5% and 2.9%. These are described as illustrative outcomes rather than separate official forecasts. The export growth forecast was raised substantially to 22%, from 14% previously — an eight-percentage-point increase. The Governor warned that growth of roughly 2% may not generate enough income for many households and businesses, and described Thailand's recovery as "K-shaped" — with export-oriented sectors booming while domestic services and tourism lag. A US tariff rate of about 19% on Thai goods was cited as a working assumption, though the final figure may differ.""",
        "verified_zh": """泰国央行将2026年GDP增长预测从2.3%上调至2.4%。制造业生产指数修订后可能再增加0.1至0.5个百分点，将整体增速提升至2.5%-2.9%之间。这些被描述为说明性结果而非单独的官方预测。出口增长预测大幅上调至22%，此前为14%——增加8个百分点。行长警告约2%的增速可能无法为许多家庭和企业创造足够收入，并将泰国的复苏描述为"K型"——出口导向行业蓬勃发展，而国内服务业和旅游业落后。美国对泰国商品约19%的关税率被引用为工作假设，但最终数字可能不同。""",
        "analysis_en": "Thailand's K-shaped recovery is perhaps the most nuanced economic story in ASEAN right now. Export growth at 22% is remarkable — but it's not translating into broad-based prosperity. The Governor's frank admission that 2% growth is insufficient for many Thai households is a striking acknowledgment of the structural challenges. The 19% US tariff assumption suggests Thailand is already pricing in significant trade friction. For businesses, the divergence between export winners and domestic laggards creates both opportunities and risks: sectors plugged into global supply chains are thriving while those dependent on domestic consumption and tourism face continued headwinds.",
        "analysis_zh": "泰国的K型复苏可能是当前东盟最微妙的经济故事。22%的出口增长令人瞩目——但未转化为普惠性繁荣。行长坦承2%增速对许多泰国家庭不够，是对结构性挑战的显著认知。19%美国关税假设表明泰国已在为重大贸易摩擦定价。出口赢家与内需落后者的分化既创造机遇也带来风险。",
        "unknowns_en": "The revised manufacturing data has not been officially released. The actual US tariff rate on Thai goods remains under negotiation. Whether tourism can accelerate enough to narrow the K-shaped gap is an open question.",
        "source_url": "https://www.thaiexaminer.com/thai-news-foreigners/2026/11/06/bank-of-thailand-boss-sees-revised-gdp-data-growth-of-up-to-2-9-as-bangkok-watches-white-house-moves/",
        "source_label": "Thai Examiner · Bank of Thailand GDP revision"
    },
    {
        "id": "vn-economy",
        "kicker_en": "Vietnam · ECONOMY",
        "kicker_zh": "越南 · 经济",
        "h2_en": "Vietnam's 10-month trade surpasses US$1 trillion as FDI surges 74% to record",
        "h2_zh": "越南前十个月贸易额突破1万亿美元，FDI飙升74%创纪录",
        "date_en": "Data: January–October 2026. General Statistics Office and Ministry of Planning, Hanoi.",
        "date_zh": "数据：2026年1至10月。统计总局和计划投资部，河内。",
        "verified_en": """Vietnam's total trade turnover exceeded US$1.01 trillion in the first ten months of 2026, up 32.3% year on year — a milestone for the economy. Exports reached approximately US$499 billion, up 27.5%. The trade deficit was US$12.07 billion. Registered FDI hit US$54.85 billion, surging 74% year on year — the strongest growth since 2009. Disbursed FDI reached US$24.08 billion, up 13.1%, the highest for the same period in five years. A total of 3,478 new FDI projects were licensed with US$30.73 billion in capital, more than doubling year on year. Singapore led foreign investment at US$9.52 billion, followed by South Korea at US$5.81 billion. Processing and manufacturing accounted for 51.6% of new and additional FDI capital. The Industrial Production Index rose 12.4%. CPI averaged 4.57% over the period, with October hitting 5.09% — above the government's approximately 4.5% full-year target. The IMF upgraded its 2026 Vietnam growth forecast from 7.1% to 8.4%.""",
        "verified_zh": """越南前十个月贸易总额突破1.01万亿美元，同比增32.3%——这是经济发展的里程碑。出口约4,990亿美元，增27.5%。贸易逆差120.7亿美元。注册FDI达548.5亿美元，同比飙升74%——为2009年以来最强增长。实际使用FDI 240.8亿美元，增13.1%，为五年来同期最高。共批准3,478个新项目，资金307.3亿美元，同比翻倍以上。新加坡以95.2亿美元领跑外资，韩国58.1亿美元次之。加工制造业占新增FDI资本的51.6%。工业生产指数增12.4%。CPI平均4.57%，10月达5.09%——超过政府约4.5%的全年目标。IMF将越南2026年增长预测从7.1%上调至8.4%。""",
        "analysis_en": "Vietnam's numbers are staggering and represent a fundamental shift in the global manufacturing map. The US$1 trillion trade milestone puts Vietnam alongside economies far larger by population. The 74% FDI surge reflects the acceleration of supply-chain diversification away from China — Vietnam is the primary beneficiary of this structural shift. However, the 5.09% October inflation reading is a warning sign: the economy may be overheating, with credit growth stalling and new lending rates exceeding 10%. The government's ambitious 10% full-year GDP target would require 12.5% Q4 growth — extremely challenging. The trade deficit of US$12 billion, driven by massive electronics imports (up 82.8%), shows the economy remains dependent on imported components for its export machine.",
        "analysis_zh": "越南的数据令人震撼，代表全球制造业版图的根本性变化。1万亿美元贸易里程碑使越南与人口远大于其的经济体并肩。FDI飙升74%反映供应链从中国多元化的加速——越南是这一结构性转变的主要受益者。但10月CPI达5.09%是警告信号：经济可能过热，信贷增长停滞，新增贷款利率超10%。政府雄心勃勃的10%全年GDP目标需要第四季12.5%的增速——极具挑战。120.7亿美元贸易逆差（电子进口猛增82.8%驱动）显示经济仍依赖进口零部件支撑出口机器。",
        "unknowns_en": "Whether Vietnam can control inflation while maintaining growth momentum is the key uncertainty. The 10% GDP target appears unrealistic without extraordinary Q4 performance. Watch the State Bank of Vietnam's response to rising CPI and lending rates.",
        "source_url": "https://english.vov.vn/en/economy/vietnams-economy-posts-record-10-month-figures-faces-final-stretch-challenges-post1347333.vov",
        "source_label": "VOV · Vietnam 10-month economic results"
    },
    {
        "id": "vn-fdi",
        "kicker_en": "Vietnam · INVESTMENT",
        "kicker_zh": "越南 · 投资",
        "h2_en": "Vietnam's FDI inflows post strongest growth since 2009 as supply chains diversify",
        "h2_zh": "越南FDI流入录得2009年以来最强增长，供应链持续多元化",
        "date_en": "Data as of 31 October 2026. Foreign Investment Agency, Ministry of Planning and Investment.",
        "date_zh": "数据截至2026年10月31日。计划投资部外国投资局。",
        "verified_en": """Vietnam's registered FDI reached US$54.85 billion in the first ten months, up 74% year on year and the strongest growth rate since 2009. New project registrations totalled US$30.73 billion across 3,478 projects, more than doubling in value. Existing projects added US$16.13 billion in additional capital, up 33.2%. Capital contributions and share purchases reached US$7.99 billion across 2,616 transactions, up 49.6%. Disbursed FDI was US$24.08 billion, up 13.1%. Singapore led with US$9.52 billion (31% of newly registered capital), followed by South Korea at US$5.81 billion (18.9%), Luxembourg at US$4.99 billion (16.2%), Hong Kong at US$3.57 billion (11.6%), and China at US$2.77 billion (9%). Processing and manufacturing dominated with US$24.19 billion in new and additional capital (51.6%). Ho Chi Minh City alone attracted US$19.1 billion, exceeding its annual target by 73.9%. Investors came from 80 countries and territories.""",
        "verified_zh": """越南前十个月注册FDI达548.5亿美元，同比增74%，为2009年以来最强增速。新批项目3,478个，注册资金307.3亿美元，金额翻倍以上。现有项目增资161.3亿美元，增33.2%。出资购股79.9亿美元，涉及2,616笔交易，增49.6%。实际到位FDI 240.8亿美元，增13.1%。新加坡以95.2亿美元居首（占新注册资本31%），韩国58.1亿美元（18.9%），卢森堡49.9亿美元（16.2%），香港35.7亿美元（11.6%），中国27.7亿美元（9%）。加工制造业以241.9亿美元的新增资本占51.6%主导地位。胡志明市独揽191亿美元，超出年度目标73.9%。投资者来自80个国家和地区。""",
        "analysis_en": "The breadth of FDI sources — 80 countries, with Singapore, South Korea, Luxembourg, Hong Kong and China all making significant commitments — demonstrates that Vietnam's appeal transcends any single geopolitical dynamic. Luxembourg's third-place ranking likely reflects European holding-company structures routing investments through the country. The dominance of processing and manufacturing (51.6%) confirms Vietnam's role as a factory-floor alternative to China. Ho Chi Minh City capturing US$19.1 billion shows the southern economic hub is pulling away from Hanoi as the primary investment magnet. Samsung, which wants to maintain its position as Vietnam's largest FDI firm, continues to anchor the electronics manufacturing ecosystem.",
        "analysis_zh": "FDI来源的广泛性——80个国家，新加坡、韩国、卢森堡、香港和中国均作出重大承诺——证明越南的吸引力超越单一地缘政治因素。卢森堡排名第三可能反映欧洲控股公司结构的路径安排。加工制造业主导（51.6%）确认越南作为中国制造替代者的角色。胡志明市独揽191亿美元显示南部经济中心正拉开与河内的差距。三星希望保持越南最大FDI企业地位，继续支撑电子制造生态系统。",
        "unknowns_en": "Registered FDI and disbursed FDI differ significantly (US$54.85bn vs US$24.08bn), and the gap between commitments and actual spending bears monitoring. Whether Vietnam's infrastructure — power, ports, roads — can absorb this investment pace is a structural question.",
        "source_url": "https://english.vov.vn/en/economy/vietnams-10-month-fdi-inflows-post-strongest-growth-since-2009-post1346873.vov",
        "source_label": "VOV · Vietnam FDI strongest growth since 2009"
    },
    {
        "id": "vn-digital",
        "kicker_en": "Vietnam · DIGITAL ECONOMY",
        "kicker_zh": "越南 · 数字经济",
        "h2_en": "Vietnam's digital economy to reach US$49 billion in 2026, leading ASEAN growth",
        "h2_zh": "越南数字经济2026年将达490亿美元，引领东盟增长",
        "date_en": "e-Conomy SEA 2026 report by Google, Temasek and Bain & Company. Published November 2026.",
        "date_zh": "谷歌、淡马锡和贝恩公司《2026年东南亚数字经济报告》，2026年11月发布。",
        "verified_en": """Vietnam's digital economy is projected to reach US$49 billion in gross merchandise value (GMV) in 2026, growing 20% year on year, according to the e-Conomy SEA report by Google, Temasek and Bain & Company. E-commerce leads at US$32 billion GMV (up 22%), accounting for roughly two-thirds of the total and projected to reach US$61 billion by 2030. Online travel is estimated at US$5 billion (up 15%), online media at US$7 billion (up 17%), and ride-hailing and food delivery at US$6 billion (up 17%). Vietnam is described as Southeast Asia's most engaged AI market, with 45 million generative-AI users — about 65% of its workforce — generating 31 billion AI prompts per year. Vietnamese accounts for 80% of AI conversations, the highest native-language share among the six largest Southeast Asian economies. Forty-four percent of consumer journeys now start with AI, and four in five users are willing to let AI agents handle shopping.""",
        "verified_zh": """根据谷歌、淡马锡和贝恩公司的东南亚数字经济报告，越南数字经济2026年商品总值（GMV）预计达490亿美元，同比增20%。电子商务以320亿美元GMV（增22%）居首，占总额约三分之二，预计2030年达610亿美元。在线旅游约50亿美元（增15%），在线媒体70亿美元（增17%），网约车和外卖60亿美元（增17%）。越南被描述为东南亚最活跃的AI市场，拥有4,500万生成式AI用户——约占劳动力的65%——每年产生310亿次AI提示词。越南语占AI对话的80%，为六大东南亚经济体中母语占比最高。44%的消费旅程以AI开始，五分之四用户愿意让AI代理处理购物。""",
        "analysis_en": "Vietnam's digital economy story is no longer just about catch-up — it's about leading. The 45 million GenAI users represent one of the highest adoption rates globally relative to workforce size. The 80% native-language AI usage suggests Vietnamese-language AI tools have reached a tipping point, unlike many developing economies where English-language tools dominate. For businesses, the finding that 44% of consumer journeys start with AI and 80% would delegate shopping to AI agents points to a fundamental reshaping of commerce and marketing in the region. The e-commerce trajectory to US$61 billion by 2030 positions Vietnam as a major global e-commerce market.",
        "analysis_zh": "越南数字经济不再仅仅是追赶——而是引领。4,500万GenAI用户代表了全球相对于劳动力规模最高的采用率之一。80%的越南语AI使用表明越南语AI工具已达到临界点，不同于许多以英语工具为主的发展中经济体。44%消费旅程以AI开始、80%用户愿委托AI购物，指向商业和营销的根本性重塑。电子商务到2030年达610亿美元将使越南成为主要全球电商市场。",
        "unknowns_en": "GMV projections are estimates by Google, Temasek and Bain — not government statistics. The actual profitability of the digital economy's participants and the sustainability of the AI adoption trajectory remain to be seen.",
        "source_url": "https://en.vietnamplus.vn/vietnams-digital-economy-to-reach-49-billion-usd-in-2026-fastest-growing-in-southeast-asia-post354926.vnp",
        "source_label": "VietnamPlus · Vietnam digital economy 2026"
    },
    {
        "id": "ph-exports",
        "kicker_en": "Philippines · NEW RELEASE",
        "kicker_zh": "菲律宾 · 新公告",
        "h2_en": "Philippine exports hit record US$9.87 billion in September on semiconductor surge",
        "h2_zh": "菲律宾9月出口创纪录达98.7亿美元，半导体激增",
        "date_en": "Released 2 Nov 2026; reference period September 2026. Philippine Statistics Authority.",
        "date_zh": "2026年11月2日公布；统计期为9月。菲律宾统计局。",
        "verified_en": """Philippine merchandise exports reached US$9.87 billion in September 2026, up 35.6% from US$7.28 billion a year earlier — the highest monthly export value since the PSA began tracking trade in 1991. This marked the 21st consecutive month of year-on-year growth. January-to-September exports totalled US$73.95 billion, up 17.2%. Electronic products led at US$6.92 billion (70.1% of total), adding US$2.89 billion year on year. The electronic sector's share of total exports — above 70% — underscores the Philippines' deepening integration into global semiconductor supply chains. Imports rose 25.7% to US$15.03 billion, widening the trade deficit to US$5.15 billion.""",
        "verified_zh": """菲律宾9月商品出口达98.7亿美元，同比增35.6%，为统计局1991年有记录以来最高月度出口额。连续21个月同比增长。前九个月出口总计739.5亿美元，增17.2%。电子产品出口69.2亿美元，占出口总额70.1%，同比增加28.9亿美元。电子行业占出口总额超70%，凸显菲律宾在全球半导体供应链中的深入融合。进口增25.7%至150.3亿美元，贸易逆差扩大至51.5亿美元。""",
        "analysis_en": "The Philippines' export surge is driven overwhelmingly by electronics and semiconductors, reflecting the country's deepening role in global chip supply chains. The heavy concentration in one sector is both a strength and a vulnerability — especially given the current AI bubble fears that are shaking tech stocks across Asia. The 70.1% electronics share is significantly higher than Vietnam's or Thailand's electronics ratios, making the Philippines uniquely exposed to semiconductor demand cycles. The widening trade deficit to US$5.15 billion adds pressure to the already-weakened peso.",
        "analysis_zh": "出口激增主要由电子和半导体驱动，体现菲律宾在全球芯片供应链中地位加深。高度集中于单一行业既是优势也是风险——尤其在AI泡沫忧虑冲击亚洲科技股之际。70.1%的电子占比显著高于越南或泰国，使菲律宾对半导体需求周期的暴露度独一无二。贸易逆差扩大至51.5亿美元加剧了比索的压力。",
        "unknowns_en": "Whether this export pace is sustainable depends on global semiconductor demand and whether the AI investment cycle continues. The widening trade deficit also bears watching as it could put pressure on the peso.",
        "source_url": "https://thephilbiznews.com/2026/11/02/ph-exports-hit-record-us9-87b/",
        "source_label": "ThePhilBizNews · PSA export data"
    },
    {
        "id": "bsp-rate",
        "kicker_en": "Philippines · MONETARY POLICY",
        "kicker_zh": "菲律宾 · 货币政策",
        "h2_en": "BSP holds tightening stance at 5.5% as inflation forecast hits 6.1%, growth slows to 2.3%",
        "h2_zh": "菲律宾央行维持5.5%紧缩立场，通胀预测达6.1%，经济增速放缓至2.3%",
        "date_en": "BSP Governor Eli Remolona Jr. remarks, 4 Nov 2026. Manila.",
        "date_zh": "央行行长Eli Remolona Jr.讲话，2026年11月4日，马尼拉。",
        "verified_en": """BSP Governor Eli Remolona Jr. said the central bank remains in a "tightening phase" and is not yet considering easing. The Monetary Board raised key policy rates by 50 basis points in October, bringing the benchmark to 5.5%. The BSP's 2026 inflation forecast stands at 6.1%, well above the 2.0–4.0% target range. The 2027 forecast was raised to 6.0% from 5.4%. Q2 2026 GDP growth slowed to 2.3%, below the government's 3.5–4.5% target, attributed to the lingering effects of last year's corruption scandal and the early-2026 Middle East war's impact on energy prices. Remolona said he focuses on core inflation: "What we really monitor is the core, because we have nothing to do with volatility." A further 25-basis-point hike in December is considered likely by analysts at UA&P, who project inflation could reach 8.0% in Q4 2026.""",
        "verified_zh": """央行行长Remolona表示央行仍处于"紧缩阶段"，尚未考虑放松。货币委员会10月将政策利率上调50个基点至5.5%。2026年通胀预测为6.1%，远高于2.0-4.0%的目标区间。2027年预测从5.4%上调至6.0%。第二季GDP增速放缓至2.3%，低于政府3.5-4.5%的目标，归因于去年腐败丑闻的持续影响和2026年初中东战争对能源价格的冲击。Remolona说他关注核心通胀："我们真正监测的是核心通胀，因为我们对波动无能为力。"UA&P分析师认为12月可能再加25个基点，预计第四季通胀或达8.0%。""",
        "analysis_en": "The Philippines faces the most challenging monetary-policy environment in ASEAN. With inflation at 6.1% and growth at just 2.3%, the BSP is caught between fighting price pressures and avoiding further economic damage. The potential for Q4 inflation reaching 8% — if UA&P's forecast proves correct — would make the Philippines an outlier in the region, where most central banks are dealing with more moderate price pressures. The corruption scandal's lingering economic impact and Middle East energy-price effects have created a uniquely difficult backdrop. For businesses, the 5.5% policy rate and potentially higher borrowing costs are a significant headwind.",
        "analysis_zh": "菲律宾面临东盟最具挑战性的货币政策环境。通胀6.1%、增速仅2.3%，央行陷入抑制物价与避免经济进一步受损之间。若UA&P第四季通胀达8%的预测成真，菲律宾将成为区域异类。腐败丑闻的持续经济影响和中东能源价格效应创造了独特困境。5.5%的政策利率及可能更高的借贷成本对企业构成显著逆风。",
        "unknowns_en": "Whether the BSP hikes again in December depends on the November inflation reading. Recovery to the growth target may not come until Q4 2026 or Q1 2027, according to the Governor.",
        "source_url": "https://www.manilatimes.net/2026/11/04/business/top-business/bsp-chief-were-still-in-tightening-phase/2461165",
        "source_label": "Manila Times · BSP tightening stance"
    },
    {
        "id": "bsp-peso",
        "kicker_en": "Philippines · FOREX",
        "kicker_zh": "菲律宾 · 外汇",
        "h2_en": "BSP says forex market stable despite peso hitting record low of P64.17",
        "h2_zh": "菲律宾央行称外汇市场稳定，尽管比索跌至历史低位64.17",
        "date_en": "BSP Deputy Governor statement, 7 Nov 2026. Press briefing in Iloilo City.",
        "date_zh": "央行副行长声明，2026年11月7日，伊洛伊洛市新闻发布会。",
        "verified_en": """BSP Deputy Governor Zeno Abenoja said dollar inflows continue to meet the foreign-currency needs of businesses and households, describing conditions as orderly. "We want the foreign exchange market to experience orderly conditions," he said at a press briefing in Iloilo City. The peso hit a record low of P64.17 per US dollar on October 27. Abenoja cited international reserves — described as "more than adequate" — along with continued growth in overseas Filipino worker (OFW) remittances and BPO revenues as supporting stability. The BSP is watching for inflationary effects from significant exchange-rate movements. Separately, analysts noted that OFW exporters could benefit from the weak peso, though imported input costs would rise.""",
        "verified_zh": """央行副行长Zeno Abenoja表示美元流入继续满足企业和家庭的外币需求，市场状况有序。"我们希望外汇市场经历有序的状况，"他在伊洛伊洛市的新闻发布会上说。比索10月27日跌至创纪录低位1美元兑64.17比索。Abenoja援引被描述为"绰绰有余"的国际储备，以及持续增长的海外菲律宾劳工（OFW）汇款和BPO收入支持稳定。央行正关注显著汇率变动的通胀效应。分析师另指出OFW和出口商可能从弱势比索中受益，但进口成本将上升。""",
        "analysis_en": "The BSP's 'orderly conditions' language is careful and measured — central banks rarely acknowledge disorder until after they've intervened. The peso's record low reflects the twin pressures of capital outflows amid the global tech selloff and the country's elevated inflation and widening trade deficit. The structural supports — OFW remittances and BPO revenues — are real but growing slowly, while the pressures are acute. The BSP is walking a tightrope: defending the peso aggressively would drain reserves, while letting it slide further risks imported inflation on top of already-elevated prices.",
        "analysis_zh": "央行'有序状况'的措辞审慎——央行很少在干预之前承认无序。比索的历史低位反映了全球科技股抛售中的资本外流以及国内高通胀和贸易逆差扩大的双重压力。结构性支撑——OFW汇款和BPO收入——真实存在但增长缓慢，而压力却很急迫。央行走钢丝：积极捍卫比索会消耗储备，而放任进一步滑落则有输入性通胀风险。",
        "unknowns_en": "The BSP did not disclose whether it has intervened in the forex market. Whether the peso stabilises depends on global risk sentiment, the Fed's rate path, and whether Philippine inflation peaks soon.",
        "source_url": "https://www.manilatimes.net/2026/11/07/regions/bsp-says-forex-market-stable-amid-peso-slump/2464272",
        "source_label": "Manila Times · BSP forex stability"
    },
    {
        "id": "kh-trade",
        "kicker_en": "Cambodia · TRADE",
        "kicker_zh": "柬埔寨 · 贸易",
        "h2_en": "Cambodia's trade turnover surges 22% to US$57 billion in nine months",
        "h2_zh": "柬埔寨前九个月贸易额飙升22%至570亿美元",
        "date_en": "Data: January–September 2026. Ministry of Commerce and General Department of Customs, Phnom Penh.",
        "date_zh": "数据：2026年1至9月。商务部和海关总署，金边。",
        "verified_en": """Cambodia's international trade turnover reached approximately US$57 billion in the first nine months of 2026, up about 21–22% year on year, according to official data cited by multiple media outlets. The growth was driven by strong garment, footwear and travel-goods (GFT) exports, which hit approximately US$13 billion for the period. Cambodia's trade with RCEP member countries surged past US$35 billion through September. Total 2025 garment and footwear exports had reached US$15.5 billion for the full year. The Kingdom's trade with Indonesia alone neared US$1 billion in eight months. Cambodia's foreign trade had already risen 19.9% to US$23 billion in Q1 2026, signalling a strong trajectory from the start of the year. Xinhua reported Cambodia's foreign trade up 22% in the first nine months.""",
        "verified_zh": """据多家媒体援引官方数据，柬埔寨前九个月国际贸易额达约570亿美元，同比增约21-22%。增长由强劲的制衣、鞋类和旅行用品（GFT）出口驱动，该期间达约130亿美元。柬埔寨与RCEP成员国的贸易截至9月突破350亿美元。2025年全年制衣和鞋类出口已达155亿美元。柬埔寨仅与印尼的贸易在八个月内就接近10亿美元。第一季外贸已增19.9%至230亿美元，显示全年强劲轨迹。新华社报道柬埔寨前九个月外贸增22%。""",
        "analysis_en": "Cambodia's 22% trade growth is one of the strongest in ASEAN and reflects the country's emergence as a manufacturing alternative for labour-intensive industries. The GFT sector remains the backbone of exports, but the diversification into tyre manufacturing (see separate report) and growing RCEP trade suggest broadening competitiveness. The RCEP trade surge past US$35 billion demonstrates how the regional trade pact is actively reshaping Southeast Asian trade patterns. Cambodia's proximity to Vietnam — itself experiencing explosive trade growth — creates potential for cross-border supply-chain integration.",
        "analysis_zh": "柬埔寨22%的贸易增长是东盟最强之一，反映该国作为劳动密集型产业制造替代地的崛起。GFT仍是出口支柱，但轮胎制造（见另一报道）和RCEP贸易增长的多元化表明竞争力在拓宽。RCEP贸易突破350亿美元显示区域贸易协定正积极重塑东南亚贸易格局。柬埔寨与越南的邻近——后者贸易也爆发式增长——为跨境供应链整合创造了潜力。",
        "unknowns_en": "Detailed breakdowns of export categories and trading partners beyond GFT are limited in available reports. Whether Cambodia can sustain this pace through Q4 depends on global demand for garments and footwear, which is sensitive to consumer confidence in the US and Europe.",
        "source_url": "https://english.news.cn/20261008/5388271703ec44f8aa1279cf4bc9e31d/c.html",
        "source_label": "Xinhua · Cambodia foreign trade growth"
    },
    {
        "id": "kh-tyre",
        "kicker_en": "Cambodia · MANUFACTURING",
        "kicker_zh": "柬埔寨 · 制造业",
        "h2_en": "Cambodia's tyre exports surge 77% to US$1.72 billion as automotive manufacturing takes off",
        "h2_zh": "柬埔寨轮胎出口飙升77%至17.2亿美元，汽车制造业起飞",
        "date_en": "Data: January–September 2026. Khmer Times citing industry data.",
        "date_zh": "数据：2026年1至9月。《高棉时报》引述行业数据。",
        "verified_en": """Cambodia's tyre exports surged 77.4% year on year to US$1.72 billion in the first nine months of 2026, according to Khmer Times, reflecting rapid expansion in the automotive manufacturing sector and growing international demand. The tyre industry represents one of Cambodia's most successful manufacturing diversification stories, moving the country beyond its traditional garment-export base. The growth has been driven by Chinese tyre manufacturers establishing factories in Cambodia to serve global markets while benefiting from the country's preferential trade agreements and lower labour costs.""",
        "verified_zh": """据《高棉时报》报道，柬埔寨前九个月轮胎出口同比飙升77.4%至17.2亿美元，反映汽车制造业的快速扩张和不断增长的国际需求。轮胎产业代表了柬埔寨最成功的制造业多元化案例之一，推动该国超越传统制衣出口基础。增长由中国轮胎制造商在柬埔寨建厂驱动，利用该国的优惠贸易协定和较低劳动力成本服务全球市场。""",
        "analysis_en": "Cambodia's tyre-export boom is a remarkable diversification success. At US$1.72 billion in nine months, tyre exports are now a significant share of Cambodia's total export base, rivalling some sub-segments of the garment sector. The Chinese tyre manufacturers' strategic decision to produce in Cambodia exploits the country's preferential market access (particularly EBA status with the EU and RCEP benefits) while avoiding tariffs that would apply to exports directly from China. This is a textbook case of how trade agreements reshape manufacturing geography. The 77% growth rate suggests the sector is still in its expansion phase, with more factories likely coming online.",
        "analysis_zh": "柬埔寨轮胎出口的爆发是一个卓越的多元化成功案例。前九个月17.2亿美元的轮胎出口已成为该国出口基础的重要份额。中国轮胎制造商在柬埔寨生产的战略决策利用了该国的优惠市场准入（尤其是对欧盟的EBA地位和RCEP优惠），同时避开了从中国直接出口的关税。这是贸易协定重塑制造业地理格局的教科书案例。77%的增速表明该行业仍处于扩张阶段。",
        "unknowns_en": "Whether the tyre sector's growth triggers trade scrutiny from importing countries (particularly over rules of origin) is a risk to watch. Environmental and labour standards in the new factories have not been independently verified in this report.",
        "source_url": "https://www.khmertimeskh.com/502041045/cambodia-tyre-exports-reach-1-72-billion-in-nine-months",
        "source_label": "Khmer Times · Cambodia tyre exports"
    },
]

# Build HTML
def build_html():
    contents_html = ""
    articles_html = ""

    for s in STORIES:
        # Contents entry
        contents_html += f'<a href="#{s["id"]}">{s["h2_en"]}<br><small>{s["h2_zh"]}</small></a>'

        # Article
        articles_html += f'''<article id="{s["id"]}"><div class="kicker">{s["kicker_en"]} / {s["kicker_zh"]}</div><div class="en"><h2>{s["h2_en"]}</h2><p class="date">{s["date_en"]}</p><h3>Verified reporting</h3><p>{s["verified_en"]}</p><div class="analysis"><h3>Our analysis</h3><p>{s["analysis_en"]}</p></div><h3>Unknowns &amp; what comes next</h3><p>{s["unknowns_en"]}</p></div><div class="zh" lang="zh-Hans"><h2>{s["h2_zh"]}</h2><p class="date">{s["date_zh"]}</p><h3>已核实事实</h3><p>{s["verified_zh"]}</p><div class="analysis"><p>原创分析：{s["analysis_zh"]}</p></div></div><p class="source">Source / 来源：<a href="{s["source_url"]}" target="_blank" rel="noopener noreferrer">{s["source_label"]}</a></p><a class="back" href="#top">↑ Contents / 目录</a></article>
'''

    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>7 November 2026 | ASEAN Business Brief</title><meta name="description" content="ASEAN Business Brief: comprehensive daily business news from official sources across Southeast Asia, in English and Chinese. 东盟商业简报：每日东盟官方商业新闻，中英双语。"><meta property="og:type" content="website"><meta property="og:site_name" content="ASEAN Business Brief"><meta property="og:title" content="ASEAN Business Brief · 7 November 2026 — Expanded Edition"><meta property="og:description" content="20 stories: Asian market selloff, Singapore banks (DBS, OCBC, UOB), Mapletree IPO, SIA cabins, Google $15bn Malaysia, Indonesia GDP & nickel, Thailand GDP & GULF Energy, Vietnam $1tn trade & FDI surge, Philippines exports & BSP, Cambodia trade boom."><meta property="og:url" content="https://asean-news.vercel.app/"><meta property="og:image" content="https://asean-news.vercel.app/asean-tv-studio.png"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#153b49"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2712%27 fill=%27%23153b49%27/%3E%3Ctext x=%2732%27 y=%2743%27 font-family=%27Georgia,serif%27 font-size=%2730%27 font-weight=%27700%27 fill=%27%23f6f4ef%27 text-anchor=%27middle%27%3EAB%3C/text%3E%3C/svg%3E"><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f6f4ef;color:#162b39;font:17px/1.75 Arial,'Microsoft YaHei',sans-serif}}header,main,footer{{max-width:1080px;margin:auto;padding:28px}}header{{border-top:8px solid #133c4a}}h1{{font:700 clamp(34px,6vw,62px)/1.1 Georgia,serif;letter-spacing:-1px;margin:22px 0 12px}}h2{{font:700 clamp(26px,4vw,35px)/1.2 Georgia,'Microsoft YaHei',serif}}h3{{font-size:15px;margin:22px 0 6px;text-transform:uppercase;letter-spacing:.7px}}.kicker{{font-size:12px;font-weight:bold;letter-spacing:1px;color:#93613d}}.date,.source,.back{{font-size:13px;color:#546873}}a{{color:#145969;text-underline-offset:3px}}.notice,.analysis{{background:#e8eeea;padding:15px 20px}}.notice{{font-size:14px}}details.notice summary{{cursor:pointer;list-style:none}}details.notice summary::-webkit-details-marker{{display:none}}details.notice .more{{color:#145969;text-decoration:underline;text-underline-offset:3px}}details.notice[open] summary{{margin-bottom:10px}}details.notice[open] .more{{display:none}}.analysis h3{{margin-top:0}}article{{padding:36px 0;border-top:1px solid #bfc9c9;scroll-margin-top:12px}}article p{{margin:8px 0 15px}}.contents{{display:grid;grid-template-columns:1fr 1fr;gap:10px 25px;padding:24px 0}}.contents a{{display:block;padding:12px 0;border-bottom:1px solid #cbd3d0}}.toolbar{{display:flex;gap:9px;flex-wrap:wrap;margin:20px 0}}button,.pill{{border:1px solid #164353;padding:8px 14px;background:transparent;color:#164353;cursor:pointer;font:inherit}}button[aria-pressed=true]{{background:#164353;color:white}}.zh{{display:none}}body.both .zh,body.chinese .zh{{display:block}}body.chinese .en{{display:none}}.zh{{border-top:2px solid #d4ded8;margin-top:22px;padding-top:10px}}body.chinese .zh{{border:0;margin:0;padding:0}}table{{border-collapse:collapse;width:100%;font-size:14px}}td,th{{padding:13px 10px;text-align:left;vertical-align:top;border-bottom:1px solid #cad2d0}}th{{background:#e8eeea}}footer{{font-size:13px;border-top:3px solid #133c4a}}@media(max-width:650px){{header,main,footer{{padding:20px}}.contents{{grid-template-columns:1fr}}td,th{{padding:10px 5px}}body{{font-size:16px}}}}@media print{{.toolbar,.back{{display:none}}.zh{{display:block}}article{{break-inside:avoid}}}}
</style></head><body class="english"><nav aria-label="Site navigation" style="padding:14px 20px;text-align:center;background:#153a50;color:white;font:15px/1.4 Arial,sans-serif"><a style="color:#ffd080;margin:0 12px" href="index.html">News / 新闻</a><a style="color:white;margin:0 12px" href="ASEAN-TV-2026-11-07.html">TV / 电视</a><a style="color:white;margin:0 12px" href="documentaries.html">Documentaries / 专题纪录</a></nav><header id="top"><div class="kicker">INDEPENDENT WORDING · PRIMARY SOURCES / 原创撰写 · 官方一手来源</div><h1>ASEAN Business Brief</h1><p>7 November 2026 / 2026年11月7日 · Asia/Singapore · <strong>Expanded Edition — 20 Stories / 扩展版 — 20篇报道</strong></p><div class="toolbar"><button onclick="setLanguage('english',this)" aria-pressed="true">English</button><button onclick="setLanguage('chinese',this)" aria-pressed="false">简体中文</button><button onclick="setLanguage('both',this)" aria-pressed="false">English + 中文</button><a class="pill" href="ASEAN-TV-2026-11-07.html">TV / 电视</a></div><details class="notice"><summary><strong>Updated 7 Nov 2026 · 18:00 SGT</strong> · 更新于新加坡时间11月7日18:00 · <span class="more">About this edition / 本期说明</span></summary><strong>Editorial cutoff: 7 November 2026 · 18:00 SGT.</strong> This expanded edition draws on news releases and verified reports across the ASEAN region. Coverage spans 8 countries with 20 stories — our most comprehensive daily edition. Earlier items are labelled separately. This is a selection, not exhaustive all-news coverage.<br><strong>截稿：新加坡时间11月7日18:00。</strong> 本扩展版选取东盟区域新闻公告及已核实报道，涵盖8个国家共20篇报道——迄今最全面的每日版本。旧消息另作标记；非所有新闻的完整汇总。</details></header><main><div class="kicker">TODAY'S NEWSPAPER — EXPANDED EDITION / 今日报纸 — 扩展版</div><div class="contents">{contents_html}</div>

{articles_html}

</main><footer>ASEAN Business Brief · 7 November 2026 · Expanded Edition — 20 stories across 8 ASEAN countries · Original reporting and separately labelled analysis. <a href="index.html">Home / 主页</a> · <a href="ASEAN-Daily-2026-11-06.html">Previous edition / 上一期</a></footer><script>function setLanguage(mode,button){{document.body.className=mode;document.documentElement.lang=mode==='chinese'?'zh-Hans':'en';document.querySelectorAll('.toolbar button[aria-pressed]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));try{{localStorage.setItem('ab-lang',mode)}}catch(e){{}}}}(function(){{var m=null;try{{m=localStorage.getItem('ab-lang')}}catch(e){{}}if(!m)m=/^zh/i.test(navigator.language||'')?'chinese':'english';var i={{english:0,chinese:1,both:2}}[m];var b=document.querySelectorAll('.toolbar button')[i];if(b)setLanguage(m,b)}})();</script><script src="news-narration.js"></script><script src="presenter-mouth.js"></script><script src="news-live.js"></script></body></html>'''

    return html

if __name__ == "__main__":
    html = build_html()
    with open("/home/claude/asean-news/ASEAN-Daily-2026-11-07.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written {len(html)} bytes, {html.count('<article')} articles")
