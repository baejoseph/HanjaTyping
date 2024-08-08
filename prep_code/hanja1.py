# Use these 어문회 hanja by grades to start the JSON file.
import json

grade1 = """呵 哥 嘉 嫁 稼 苛 袈 駕 伽 柯 賈 軻 迦 佳 架 暇 假 街 加 可 價 家 歌 恪 殼 珏 却 脚 閣 刻 覺 各 角 墾 奸 揀 澗 癎 竿 艱 諫 杆 艮 姦 刊 幹 懇 肝 干 看 簡 間 喝 竭 褐 鞨 葛 渴 勘 堪 柑 疳 瞰 紺 憾 鑑 敢 甘 減 監 感 匣 閘 岬 鉀 甲 慷 糠 腔 薑 姜 岡 崗 彊 疆 剛 綱 鋼 降 康 講 強 江 凱 愾 漑 箇 芥 价 塏 慨 皆 介 槪 蓋 個 改 開 客 羹 坑 醵 倨 渠 距 居 巨 拒 據 去 擧 車 巾 腱 虔 鍵 乾 件 健 建 杰 桀 乞 傑 劍 儉 檢 劫 怯 偈 憩 揭 檄 膈 覡 隔 擊 激 格 繭 譴 鵑 甄 牽 絹 肩 遣 堅 犬 見 訣 潔 缺 決 結 兼 謙 勁 憬 梗 痙 磬 脛 莖 頸 鯨 儆 炅 璟 瓊 卿 庚 竟 徑 硬 耕 頃 傾 更 鏡 驚 境 慶 經 警 景 競 輕 敬 京 悸 癸 繫 啓 契 桂 械 溪 季 戒 系 繼 階 鷄 係 界 計 叩 呱 拷 敲 痼 股 膏 袴 辜 錮 皐 雇 枯 顧 姑 稿 鼓 孤 庫 故 固 考 告 古 苦 高 梏 鵠 哭 谷 穀 曲 昆 棍 袞 坤 困 汨 骨 拱 鞏 供 恐 恭 貢 孔 攻 公 共 功 工 空 顆 戈 瓜 菓 寡 誇 課 過 果 科 廓 槨 藿 郭 棺 灌 顴 串 琯 款 冠 寬 慣 貫 館 管 官 觀 關 刮 括 匡 壙 曠 胱 狂 鑛 廣 光 卦 罫 掛 乖 拐 魁 槐 傀 塊 愧 壞 怪 宏 肱 轟 咬 喬 嬌 攪 狡 皎 蛟 轎 驕 僑 絞 膠 矯 郊 巧 較 橋 交 敎 校 仇 嘔 垢 寇 嶇 枸 柩 毆 溝 灸 矩 臼 舅 衢 謳 軀 鉤 駒 鳩 廏 玖 邱 歐 購 鷗 俱 懼 狗 苟 驅 龜 丘 久 拘 構 句 求 究 救 具 舊 區 球 口 九 鞠 菊 局 國 窘 君 群 郡 軍 掘 窟 屈 穹 躬 弓 窮 宮 倦 捲 眷 圈 拳 券 勸 卷 權 蹶 闕 厥 机 櫃 潰 詭 几 軌 鬼 歸 貴 硅 窺 葵 逵 圭 奎 揆 珪 閨 叫 糾 規 菌 均 橘 剋 戟 棘 隙 克 劇 極 覲 饉 槿 瑾 僅 斤 謹 勤 筋 根 近 擒 衾 襟 琴 禽 錦 禁 今 金 扱 汲 及 給 急 級 亘 矜 兢 肯 伎 嗜 妓 崎 朞 杞 畸 綺 羈 肌 譏 冀 岐 沂 淇 琦 琪 璣 箕 耆 騏 驥 麒 棋 幾 忌 旣 棄 欺 豈 飢 企 其 畿 祈 騎 奇 寄 機 紀 器 起 技 期 汽 基 己 旗 氣 記 緊 拮 吉 喫
 儺 懦 拏 拿 那 諾 煖 暖 難 捏 捺 男 南 衲 納 囊 娘 乃 奈 耐 內 女 撚 年 涅 念 寧 弩 駑 奴 努 怒 膿 濃 農 惱 腦 撓 尿 訥 紐 能 尼 泥 匿 溺
 茶 多 簞 緞 蛋 湍 鍛 丹 但 旦 段 單 斷 檀 端 壇 團 短 撻 疸 達 憺 曇 澹 痰 譚 潭 膽 淡 擔 談 遝 畓 踏 答 撞 棠 螳 塘 唐 糖 黨 當 堂 擡 袋 垈 戴 臺 貸 帶 隊 代 對 待 大 悳 德 堵 屠 掉 搗 淘 滔 濤 睹 禱 萄 賭 蹈 鍍 燾 悼 塗 挑 稻 跳 倒 刀 桃 渡 途 陶 徒 盜 逃 導 島 都 到 圖 度 道 瀆 禿 篤 毒 督 獨 讀 沌 惇 燉 頓 敦 豚 乭 突 憧 疼 瞳 胴 董 桐 棟 凍 銅 童 冬 動 同 洞 東 兜 痘 杜 斗 豆 頭 臀 遁 屯 鈍 得 橙 鄧 藤 謄 騰 燈 等 登
 懶 癩 螺 邏 裸 羅 烙 酪 駱 洛 絡 落 樂 瀾 鸞 爛 欄 蘭 亂 卵 剌 辣 籃 藍 濫 覽 臘 蠟 拉 狼 廊 浪 郞 朗 萊 來 冷 掠 略 倆 粱 亮 樑 輛 諒 梁 涼 糧 兩 量 良 侶 戾 濾 閭 黎 呂 廬 礪 驪 勵 慮 麗 旅 瀝 礫 曆 歷 力 輦 漣 煉 憐 戀 聯 蓮 鍊 連 練 劣 裂 烈 列 斂 殮 簾 濂 廉 獵 囹 逞 鈴 齡 玲 零 嶺 靈 令 領 醴 隷 例 禮 撈 擄 虜 盧 蘆 魯 鷺 爐 露 勞 路 老 碌 麓 鹿 祿 錄 綠 論 壟 瓏 聾 籠 弄 儡 牢 磊 賂 賴 雷 寮 燎 瞭 聊 寥 遼 療 了 僚 料 龍 壘 陋 屢 淚 樓 漏 累 溜 琉 瘤 劉 硫 謬 柳 留 流 類 戮 陸 六 淪 綸 崙 倫 輪 慄 栗 率 律 隆 勒 肋 凜 凌 稜 綾 菱 楞 陵 俚 悧 痢 籬 罹 裡 釐 梨 吏 履 裏 離 利 李 理 里 吝 燐 躪 鱗 麟 隣 淋 臨 林 笠 粒 立
 摩 痲 魔 磨 麻 馬 寞 膜 幕 漠 莫 卍 彎 挽 瞞 蔓 輓 饅 鰻 娩 灣 蠻 慢 漫 晩 滿 萬 抹 沫 襪 靺 末 芒 惘 網 忘 忙 罔 茫 妄 亡 望 寐 昧 煤 罵 邁 呆 枚 魅 埋 媒 梅 妹 買 賣 每 貊 麥 脈 萌 孟 猛 盲 盟 覓 棉 眄 緬 麪 冕 沔 俛 免 眠 綿 勉 面 蔑 滅 暝 溟 皿 螟 酩 冥 銘 鳴 明 名 命 袂 摸 牡 耗 糢 牟 茅 謨 帽 矛 侮 冒 募 暮 某 慕 謀 貌 模 毛 母 穆 沐 睦 牧 目 木 歿 沒 夢 蒙 描 杳 渺 猫 昴 卯 廟 苗 墓 妙 巫 憮 拇 撫 毋 畝 蕪 誣 戊 霧 茂 貿 舞 務 武 無 墨 默 蚊 汶 紊 紋 聞 問 文 門 勿 物 媚 薇 靡 彌 眉 迷 尾 微 味 未 米 美 悶 旻 旼 玟 珉 閔 憫 敏 民 謐 蜜 密
 剝 搏 撲 樸 珀 箔 粕 縛 膊 駁 舶 泊 薄 迫 拍 博 朴 拌 攀 斑 槃 畔 礬 絆 蟠 頒 潘 磻 搬 伴 叛 返 盤 般 飯 半 反 班 勃 撥 潑 跋 醱 魃 渤 鉢 拔 髮 發 坊 尨 幇 彷 昉 枋 榜 肪 膀 謗 旁 龐 紡 倣 傍 邦 芳 妨 房 訪 防 放 方 徘 湃 胚 陪 裵 俳 賠 杯 培 排 輩 拜 背 配 倍 帛 魄 柏 伯 百 白 蕃 藩 煩 飜 繁 番 筏 閥 伐 罰 帆 梵 氾 泛 范 汎 凡 犯 範 法 劈 擘 璧 癖 闢 僻 碧 壁 卞 弁 辨 辯 邊 變 瞥 鼈 別 甁 餠 昞 昺 柄 炳 秉 倂 屛 竝 丙 兵 病 堡 洑 菩 潽 甫 輔 補 譜 普 保 報 寶 步 僕 匐 輻 鰒 馥 卜 腹 覆 伏 複 復 福 服 本 捧 棒 烽 鋒 蓬 俸 縫 蜂 封 峯 逢 鳳 奉 俯 剖 咐 埠 孵 斧 腑 芙 訃 賻 駙 傅 釜 阜 敷 膚 赴 付 扶 浮 符 簿 腐 賦 附 否 負 副 婦 富 府 部 夫 父 北 吩 噴 忿 扮 焚 盆 糞 雰 芬 墳 奔 奮 紛 憤 粉 分 彿 弗 拂 佛 不 棚 硼 繃 鵬 崩 朋 匕 庇 憊 扉 沸 琵 痺 砒 秕 緋 翡 脾 臂 蜚 裨 誹 譬 鄙 妣 丕 毖 毘 泌 匪 卑 妃 婢 肥 批 碑 祕 備 悲 非 飛 比 費 鼻 嚬 嬪 殯 濱 瀕 彬 賓 頻 貧 憑 馮 聘 氷
 些 嗣 奢 娑 徙 瀉 獅 祠 紗 蓑 麝 泗 唆 赦 飼 似 巳 捨 斯 詐 賜 司 斜 沙 祀 蛇 詞 邪 射 私 絲 辭 寺 師 舍 謝 寫 思 査 仕 史 士 使 死 社 事 四 朔 削 刪 珊 疝 傘 酸 散 産 算 山 撒 煞 薩 殺 滲 蔘 森 三 澁 揷 孀 爽 翔 觴 庠 箱 嘗 祥 像 償 喪 尙 桑 裳 詳 霜 傷 象 常 床 想 狀 賞 商 相 上 璽 嗇 塞 索 色 牲 甥 生 壻 嶼 抒 曙 棲 犀 胥 薯 黍 鼠 舒 瑞 庶 敍 暑 誓 逝 徐 恕 緖 署 序 書 西 潟 奭 晳 錫 碩 昔 析 惜 釋 席 石 夕 扇 煽 羨 腺 膳 銑 瑄 璇 璿 繕 旋 禪 宣 善 船 選 仙 鮮 線 先 屑 泄 洩 渫 卨 薛 舌 設 說 雪 殲 閃 暹 蟾 陝 纖 燮 攝 涉 醒 晟 城 星 盛 聖 聲 誠 性 成 省 姓 貰 勢 稅 細 歲 洗 世 塑 宵 搔 梳 甦 疎 瘙 簫 蕭 逍 遡 巢 沼 邵 紹 召 昭 蔬 騷 燒 疏 蘇 訴 掃 笑 素 消 少 所 小 贖 粟 屬 俗 續 束 速 遜 損 孫 悚 宋 誦 訟 松 頌 送 灑 碎 刷 鎖 衰 嫂 戍 狩 瘦 穗 竪 粹 繡 羞 蒐 袖 酬 髓 讎 洙 銖 隋 囚 搜 睡 誰 遂 雖 須 垂 壽 帥 愁 殊 獸 輸 隨 需 秀 修 受 守 授 收 首 樹 手 數 水 塾 夙 菽 孰 淑 熟 叔 肅 宿 筍 醇 馴 洵 淳 珣 舜 荀 盾 循 殉 脣 巡 旬 瞬 純 順 戌 述 術 崇 膝 瑟 濕 拾 襲 習 丞 繩 升 乘 僧 昇 承 勝 匙 媤 弑 猜 諡 豺 柿 柴 屍 矢 侍 施 是 視 試 詩 示 始 市 時 拭 熄 蝕 湜 軾 殖 飾 息 識 式 植 食 呻 娠 宸 燼 薪 蜃 訊 迅 紳 腎 伸 晨 辛 愼 申 臣 信 新 神 身 悉 實 失 室 瀋 尋 審 甚 深 心 什 十 雙 氏
 俄 啞 衙 訝 餓 亞 我 牙 芽 阿 雅 兒 堊 愕 顎 握 岳 惡 按 晏 鞍 雁 岸 顔 眼 案 安 斡 軋 閼 謁 庵 闇 癌 巖 暗 鴨 押 壓 怏 秧 鴦 昂 殃 仰 央 崖 曖 隘 靄 埃 艾 礙 涯 哀 愛 扼 縊 腋 厄 額 液 櫻 鶯 冶 揶 爺 倻 惹 也 耶 夜 野 葯 躍 若 約 弱 藥 恙 攘 瘍 釀 癢 襄 孃 楊 壤 揚 讓 樣 羊 養 洋 陽 圄 瘀 禦 於 御 漁 魚 語 臆 憶 抑 億 堰 諺 彦 焉 言 儼 奄 掩 嚴 業 予 余 汝 輿 與 如 餘 繹 亦 役 疫 譯 驛 域 易 逆 捐 椽 筵 鳶 姸 淵 衍 硯 宴 沿 燕 軟 延 燃 緣 鉛 演 煙 硏 然 閱 悅 熱 焰 艶 閻 厭 染 炎 鹽 燁 葉 嬰 暎 瑛 盈 泳 詠 影 映 營 迎 榮 永 英 曳 穢 裔 詣 濊 睿 芮 預 銳 譽 豫 藝 伍 奧 寤 懊 吳 墺 梧 傲 吾 嗚 娛 汚 悟 烏 誤 午 五 沃 鈺 獄 玉 屋 蘊 穩 溫 壅 甕 邕 雍 擁 翁 渦 蝸 訛 臥 瓦 婉 宛 玩 腕 阮 頑 莞 緩 完 曰 枉 旺 汪 往 王 矮 倭 歪 巍 猥 畏 外 僥 凹 夭 拗 擾 窈 窯 邀 饒 堯 姚 耀 妖 搖 腰 遙 謠 曜 要 慾 欲 辱 浴 涌 聳 茸 蓉 踊 溶 瑢 鎔 鏞 傭 熔 庸 容 勇 用 寓 虞 迂 隅 嵎 佑 祐 禹 于 又 尤 偶 宇 愚 憂 羽 優 遇 郵 牛 友 雨 右 旭 昱 煜 郁 頊 殞 耘 隕 芸 云 韻 雲 運 蔚 鬱 熊 雄 猿 鴛 冤 媛 瑗 袁 苑 怨 援 源 員 圓 原 院 願 元 園 遠 越 月 萎 渭 韋 魏 尉 緯 違 僞 胃 謂 危 圍 委 威 慰 爲 衛 位 偉 喩 宥 愉 揄 柚 游 癒 諛 諭 蹂 鍮 兪 庾 楡 踰 唯 惟 愈 酉 幼 幽 悠 柔 猶 維 裕 誘 乳 儒 遊 遺 油 由 有 肉 育 允 尹 胤 鈗 閏 潤 戎 絨 融 垠 殷 誾 隱 恩 銀 乙 蔭 吟 淫 陰 音 飮 揖 泣 邑 膺 鷹 凝 應 擬 椅 毅 誼 宜 矣 依 儀 疑 義 議 意 衣 醫 姨 弛 爾 痍 餌 伊 怡 珥 貳 夷 而 已 異 移 耳 以 二 翌 翊 翼 益 咽 湮 蚓 靭 刃 姻 寅 忍 仁 印 引 認 因 人 佚 溢 佾 鎰 壹 逸 一 日 妊 壬 賃 任 入 剩 孕
 仔 炙 煮 瓷 疵 蔗 藉 滋 磁 諮 雌 恣 玆 刺 慈 紫 姉 姿 資 者 子 字 自 勺 嚼 灼 炸 綽 芍 雀 鵲 爵 酌 作 昨 棧 盞 殘 箴 簪 蠶 暫 潛 雜 仗 匠 杖 檣 漿 薔 醬 庄 獐 璋 蔣 墻 丈 掌 粧 臟 莊 葬 藏 壯 帳 張 腸 裝 獎 將 障 章 場 長 滓 齋 哉 宰 栽 裁 載 再 災 材 財 在 才 錚 爭 咀 狙 箸 詛 躇 邸 觝 豬 沮 抵 著 底 低 貯 嫡 狄 謫 迹 滴 寂 摘 笛 跡 蹟 積 籍 績 賊 適 敵 赤 的 剪 塡 奠 廛 悛 栓 氈 澱 煎 癲 箋 箭 篆 纏 輾 銓 顚 顫 餞 甸 殿 專 轉 錢 田 傳 典 展 戰 全 前 電 截 竊 折 絶 切 節 粘 霑 漸 占 點 店 蝶 接 幀 挺 町 睛 碇 穽 酊 釘 錠 靖 旌 晶 楨 汀 珽 禎 鄭 鼎 偵 呈 艇 訂 井 亭 廷 征 淨 貞 頂 丁 整 靜 政 程 精 停 情 定 庭 正 啼 悌 梯 蹄 劑 堤 諸 齊 帝 制 提 濟 祭 製 除 際 第 題 弟 凋 嘲 曹 棗 槽 漕 爪 眺 稠 粗 糟 繰 肇 藻 詔 躁 遭 阻 曺 祚 趙 彫 措 釣 弔 燥 兆 照 租 條 潮 組 助 早 造 鳥 操 調 朝 祖 簇 族 足 存 尊 猝 拙 卒 慫 腫 踪 踵 琮 綜 縱 從 鍾 宗 終 種 挫 佐 坐 座 左 罪 做 胄 呪 嗾 廚 紂 紬 註 誅 躊 輳 疇 駐 舟 奏 宙 柱 株 洲 珠 鑄 周 朱 酒 走 州 週 晝 注 主 住 竹 樽 竣 蠢 埈 峻 晙 浚 濬 駿 准 俊 遵 準 仲 衆 重 中 卽 櫛 汁 葺 贈 憎 曾 症 蒸 證 增 咫 摯 枳 祉 肢 址 芝 旨 脂 只 遲 之 枝 池 持 智 誌 志 指 支 至 止 知 地 紙 稙 稷 織 職 直 嗔 疹 晋 秦 塵 津 診 振 辰 鎭 陳 震 珍 盡 陣 眞 進 叱 嫉 帙 桎 膣 跌 迭 窒 姪 疾 秩 質 斟 朕 輯 執 集 澄 懲 徵
 叉 嗟 蹉 遮 且 借 此 差 次 搾 窄 鑿 捉 錯 着 撰 纂 饌 篡 燦 璨 瓚 鑽 餐 贊 讚 擦 刹 札 察 僭 塹 懺 站 讒 讖 斬 慘 慙 參 倡 娼 廠 愴 槍 漲 猖 瘡 脹 艙 菖 敞 昶 彰 滄 暢 倉 昌 蒼 創 唱 窓 寨 埰 蔡 采 債 彩 菜 採 柵 策 冊 責 凄 悽 妻 處 擲 滌 瘠 脊 陟 隻 斥 尺 戚 拓 喘 擅 穿 闡 釧 薦 淺 賤 踐 遷 泉 千 天 川 凸 綴 轍 喆 澈 撤 哲 徹 鐵 僉 籤 諂 瞻 尖 添 帖 捷 牒 疊 貼 諜 妾 晴 廳 聽 請 淸 靑 涕 諦 締 替 逮 遞 滯 體 憔 梢 樵 炒 硝 礁 稍 蕉 貂 醋 楚 哨 焦 抄 秒 礎 肖 超 招 初 草 囑 蜀 燭 促 觸 忖 村 寸 叢 塚 寵 聰 總 銃 撮 崔 催 最 墜 椎 樞 芻 酋 錐 錘 鎚 鰍 槌 楸 鄒 趨 抽 醜 追 推 秋 蹴 軸 丑 逐 畜 縮 築 蓄 祝 椿 春 黜 出 沖 衷 衝 忠 蟲 充 悴 膵 萃 贅 娶 翠 脆 聚 炊 臭 吹 醉 就 趣 取 惻 側 測 層 侈 嗤 幟 熾 痔 癡 緻 馳 峙 雉 値 恥 稚 治 置 齒 致 勅 則 親 漆 七 砧 鍼 枕 沈 浸 寢 針 侵 蟄 秤 稱
 快
 唾 惰 楕 舵 陀 駝 墮 妥 他 打 擢 鐸 琢 託 托 濁 濯 卓 呑 坦 憚 綻 灘 誕 彈 歎 炭 奪 脫 眈 耽 貪 探 搭 塔 宕 蕩 湯 汰 笞 苔 跆 兌 台 胎 颱 怠 殆 泰 態 太 澤 擇 宅 撐 攄 兔 吐 討 土 慟 桶 筒 痛 統 通 堆 腿 褪 頹 退 套 妬 透 投 鬪 慝 特
 婆 巴 爬 琶 芭 跛 坡 把 播 罷 頗 派 波 破 辦 阪 販 版 判 板 八 佩 唄 悖 沛 牌 稗 霸 貝 敗 澎 膨 彭 愎 鞭 騙 扁 遍 偏 片 編 篇 便 貶 萍 坪 評 平 斃 陛 幣 蔽 廢 弊 肺 閉 匍 咆 哺 圃 泡 疱 脯 蒲 袍 褒 逋 庖 葡 鮑 怖 抛 鋪 抱 飽 捕 浦 胞 包 布 砲 曝 瀑 幅 爆 暴 剽 慓 豹 飄 杓 漂 標 票 表 稟 品 諷 楓 豊 風 披 彼 皮 被 疲 避 疋 弼 匹 畢 必 筆 乏 逼
 瑕 蝦 遐 霞 何 荷 賀 河 下 夏 壑 謔 瘧 虐 鶴 學 悍 澣 罕 邯 翰 旱 汗 恨 閑 限 寒 漢 韓 轄 割 函 喊 檻 涵 緘 銜 鹹 艦 咸 含 陷 盒 蛤 合 缸 肛 亢 沆 巷 恒 項 抗 港 航 偕 咳 懈 楷 諧 邂 駭 骸 亥 奚 該 解 害 海 劾 核 杏 幸 行 嚮 饗 享 響 鄕 香 向 噓 墟 虛 許 軒 獻 憲 歇 險 驗 爀 赫 革 眩 絢 衒 峴 炫 鉉 弦 絃 縣 懸 玄 顯 賢 現 穴 血 嫌 俠 挾 狹 頰 陜 峽 脅 協 荊 瀅 炯 瑩 邢 馨 型 亨 螢 衡 刑 形 兄 彗 醯 兮 慧 惠 弧 狐 琥 瑚 糊 壕 扈 昊 晧 澔 皓 祜 鎬 濠 乎 互 毫 浩 胡 虎 豪 呼 好 戶 護 湖 號 酷 惑 或 渾 昏 魂 婚 混 惚 笏 忽 哄 虹 訌 泓 弘 鴻 洪 紅 嬅 樺 靴 禾 禍 華 貨 化 和 畫 花 話 火 擴 穫 確 喚 宦 驩 鰥 桓 煥 幻 丸 換 還 歡 環 患 猾 闊 滑 活 凰 徨 恍 惶 慌 煌 遑 晃 滉 皇 荒 況 黃 徊 恢 晦 繪 膾 蛔 誨 賄 檜 淮 廻 悔 懷 灰 回 會 劃 獲 橫 哮 嚆 爻 酵 曉 效 孝 吼 嗅 朽 逅 后 喉 侯 候 厚 後 暈 壎 熏 薰 勳 訓 喧 卉 喙 毁 彙 諱 麾 徽 輝 揮 烋 携 休 恤 兇 洶 匈 胸 凶 黑 欣 痕 欠 歆 欽 恰 洽 吸 興 犧 嬉 憙 熹 禧 羲 噫 姬 熙 稀 戲 喜 希 詰
"""

grade2 = """伽 柯 賈 軻 迦 佳 架 暇 假 街 加 可 價 家 歌 珏 却 脚 閣 刻 覺 各 角 杆 艮 姦 刊 幹 懇 肝 干 看 簡 間 鞨 葛 渴 憾 鑑 敢 甘 減 監 感 岬 鉀 甲 姜 岡 崗 彊 疆 剛 綱 鋼 降 康 講 強 江 价 塏 慨 皆 介 槪 蓋 個 改 開 客 坑 距 居 巨 拒 據 去 擧 車 鍵 乾 件 健 建 杰 桀 乞 傑 劍 儉 檢 憩 揭 隔 擊 激 格 甄 牽 絹 肩 遣 堅 犬 見 訣 潔 缺 決 結 兼 謙 儆 炅 璟 瓊 卿 庚 竟 徑 硬 耕 頃 傾 更 鏡 驚 境 慶 經 警 景 競 輕 敬 京 癸 繫 啓 契 桂 械 溪 季 戒 系 繼 階 鷄 係 界 計 皐 雇 枯 顧 姑 稿 鼓 孤 庫 故 固 考 告 古 苦 高 哭 谷 穀 曲 坤 困 骨 供 恐 恭 貢 孔 攻 公 共 功 工 空 戈 瓜 菓 寡 誇 課 過 果 科 郭 串 琯 款 冠 寬 慣 貫 館 管 官 觀 關 狂 鑛 廣 光 掛 槐 傀 塊 愧 壞 怪 僑 絞 膠 矯 郊 巧 較 橋 交 敎 校 玖 邱 歐 購 鷗 俱 懼 狗 苟 驅 龜 丘 久 拘 構 句 求 究 救 具 舊 區 球 口 九 鞠 菊 局 國 君 群 郡 軍 掘 窟 屈 弓 窮 宮 圈 拳 券 勸 卷 權 闕 厥 軌 鬼 歸 貴 圭 奎 揆 珪 閨 叫 糾 規 菌 均 克 劇 極 槿 瑾 僅 斤 謹 勤 筋 根 近 琴 禽 錦 禁 今 金 及 給 急 級 兢 肯 冀 岐 沂 淇 琦 琪 璣 箕 耆 騏 驥 麒 棋 幾 忌 旣 棄 欺 豈 飢 企 其 畿 祈 騎 奇 寄 機 紀 器 起 技 期 汽 基 己 旗 氣 記 緊 吉
 那 諾 暖 難 男 南 納 娘 乃 奈 耐 內 女 年 念 寧 奴 努 怒 濃 農 惱 腦 尿 能 尼 泥 溺
 茶 多 湍 鍛 丹 但 旦 段 單 斷 檀 端 壇 團 短 達 潭 膽 淡 擔 談 畓 踏 答 塘 唐 糖 黨 當 堂 垈 戴 臺 貸 帶 隊 代 對 待 大 悳 德 燾 悼 塗 挑 稻 跳 倒 刀 桃 渡 途 陶 徒 盜 逃 導 島 都 到 圖 度 道 篤 毒 督 獨 讀 惇 燉 頓 敦 豚 乭 突 董 桐 棟 凍 銅 童 冬 動 同 洞 東 杜 斗 豆 頭 屯 鈍 得 鄧 藤 謄 騰 燈 等 登
 裸 羅 洛 絡 落 樂 爛 欄 蘭 亂 卵 藍 濫 覽 拉 廊 浪 郞 朗 萊 來 冷 掠 略 亮 樑 輛 諒 梁 涼 糧 兩 量 良 呂 廬 礪 驪 勵 慮 麗 旅 曆 歷 力 漣 煉 憐 戀 聯 蓮 鍊 連 練 劣 裂 烈 列 濂 廉 獵 玲 零 嶺 靈 令 領 醴 隷 例 禮 盧 蘆 魯 鷺 爐 露 勞 路 老 鹿 祿 錄 綠 論 籠 弄 賴 雷 遼 療 了 僚 料 龍 屢 淚 樓 漏 累 劉 硫 謬 柳 留 流 類 陸 六 崙 倫 輪 栗 率 律 隆 楞 陵 梨 吏 履 裏 離 利 李 理 里 麟 隣 臨 林 立
 摩 痲 魔 磨 麻 馬 膜 幕 漠 莫 娩 灣 蠻 慢 漫 晩 滿 萬 靺 末 網 忘 忙 罔 茫 妄 亡 望 枚 魅 埋 媒 梅 妹 買 賣 每 貊 麥 脈 孟 猛 盲 盟 覓 冕 沔 俛 免 眠 綿 勉 面 蔑 滅 冥 銘 鳴 明 名 命 牟 茅 謨 帽 矛 侮 冒 募 暮 某 慕 謀 貌 模 毛 母 穆 沐 睦 牧 目 木 沒 夢 蒙 昴 卯 廟 苗 墓 妙 戊 霧 茂 貿 舞 務 武 無 墨 默 汶 紊 紋 聞 問 文 門 勿 物 彌 眉 迷 尾 微 味 未 米 美 旻 旼 玟 珉 閔 憫 敏 民 蜜 密
 舶 泊 薄 迫 拍 博 朴 潘 磻 搬 伴 叛 返 盤 般 飯 半 反 班 渤 鉢 拔 髮 發 旁 龐 紡 倣 傍 邦 芳 妨 房 訪 防 放 方 裵 俳 賠 杯 培 排 輩 拜 背 配 倍 柏 伯 百 白 煩 飜 繁 番 筏 閥 伐 罰 范 汎 凡 犯 範 法 僻 碧 壁 卞 弁 辨 辯 邊 變 別 昞 昺 柄 炳 秉 倂 屛 竝 丙 兵 病 潽 甫 輔 補 譜 普 保 報 寶 步 馥 卜 腹 覆 伏 複 復 福 服 本 蓬 俸 縫 蜂 封 峯 逢 鳳 奉 傅 釜 阜 敷 膚 赴 付 扶 浮 符 簿 腐 賦 附 否 負 副 婦 富 府 部 夫 父 北 芬 墳 奔 奮 紛 憤 粉 分 弗 拂 佛 不 鵬 崩 朋 丕 毖 毘 泌 匪 卑 妃 婢 肥 批 碑 祕 備 悲 非 飛 比 費 鼻 彬 賓 頻 貧 馮 聘 氷
 泗 唆 赦 飼 似 巳 捨 斯 詐 賜 司 斜 沙 祀 蛇 詞 邪 射 私 絲 辭 寺 師 舍 謝 寫 思 査 仕 史 士 使 死 社 事 四 朔 削 傘 酸 散 産 算 山 殺 蔘 森 三 揷 庠 箱 嘗 祥 像 償 喪 尙 桑 裳 詳 霜 傷 象 常 床 想 狀 賞 商 相 上 塞 索 色 生 舒 瑞 庶 敍 暑 誓 逝 徐 恕 緖 署 序 書 西 奭 晳 錫 碩 昔 析 惜 釋 席 石 夕 瑄 璇 璿 繕 旋 禪 宣 善 船 選 仙 鮮 線 先 卨 薛 舌 設 說 雪 暹 蟾 陝 纖 燮 攝 涉 晟 城 星 盛 聖 聲 誠 性 成 省 姓 貰 勢 稅 細 歲 洗 世 巢 沼 邵 紹 召 昭 蔬 騷 燒 疏 蘇 訴 掃 笑 素 消 少 所 小 粟 屬 俗 續 束 速 損 孫 宋 誦 訟 松 頌 送 刷 鎖 衰 洙 銖 隋 囚 搜 睡 誰 遂 雖 須 垂 壽 帥 愁 殊 獸 輸 隨 需 秀 修 受 守 授 收 首 樹 手 數 水 孰 淑 熟 叔 肅 宿 洵 淳 珣 舜 荀 盾 循 殉 脣 巡 旬 瞬 純 順 戌 述 術 崇 瑟 濕 拾 襲 習 繩 升 乘 僧 昇 承 勝 柴 屍 矢 侍 施 是 視 試 詩 示 始 市 時 湜 軾 殖 飾 息 識 式 植 食 紳 腎 伸 晨 辛 愼 申 臣 信 新 神 身 實 失 室 瀋 尋 審 甚 深 心 十 雙 氏
 餓 亞 我 牙 芽 阿 雅 兒 握 岳 惡 雁 岸 顔 眼 案 安 閼 謁 癌 巖 暗 鴨 押 壓 殃 仰 央 埃 艾 礙 涯 哀 愛 厄 額 液 倻 惹 也 耶 夜 野 躍 若 約 弱 藥 襄 孃 楊 壤 揚 讓 樣 羊 養 洋 陽 於 御 漁 魚 語 憶 抑 億 彦 焉 言 嚴 業 予 余 汝 輿 與 如 餘 亦 役 疫 譯 驛 域 易 逆 姸 淵 衍 硯 宴 沿 燕 軟 延 燃 緣 鉛 演 煙 硏 然 閱 悅 熱 閻 厭 染 炎 鹽 燁 葉 暎 瑛 盈 泳 詠 影 映 營 迎 榮 永 英 濊 睿 芮 預 銳 譽 豫 藝 吳 墺 梧 傲 吾 嗚 娛 汚 悟 烏 誤 午 五 沃 鈺 獄 玉 屋 穩 溫 甕 邕 雍 擁 翁 臥 瓦 莞 緩 完 曰 旺 汪 往 王 倭 歪 畏 外 堯 姚 耀 妖 搖 腰 遙 謠 曜 要 慾 欲 辱 浴 溶 瑢 鎔 鏞 傭 熔 庸 容 勇 用 佑 祐 禹 于 又 尤 偶 宇 愚 憂 羽 優 遇 郵 牛 友 雨 右 旭 昱 煜 郁 頊 芸 云 韻 雲 運 蔚 鬱 熊 雄 媛 瑗 袁 苑 怨 援 源 員 圓 原 院 願 元 園 遠 越 月 渭 韋 魏 尉 緯 違 僞 胃 謂 危 圍 委 威 慰 爲 衛 位 偉 兪 庾 楡 踰 唯 惟 愈 酉 幼 幽 悠 柔 猶 維 裕 誘 乳 儒 遊 遺 油 由 有 肉 育 允 尹 胤 鈗 閏 潤 融 垠 殷 誾 隱 恩 銀 乙 吟 淫 陰 音 飮 泣 邑 鷹 凝 應 宜 矣 依 儀 疑 義 議 意 衣 醫 伊 怡 珥 貳 夷 而 已 異 移 耳 以 二 翊 翼 益 刃 姻 寅 忍 仁 印 引 認 因 人 佾 鎰 壹 逸 一 日 妊 壬 賃 任 入
 滋 磁 諮 雌 恣 玆 刺 慈 紫 姉 姿 資 者 子 字 自 爵 酌 作 昨 殘 蠶 暫 潛 雜 庄 獐 璋 蔣 墻 丈 掌 粧 臟 莊 葬 藏 壯 帳 張 腸 裝 獎 將 障 章 場 長 哉 宰 栽 裁 載 再 災 材 財 在 才 爭 沮 抵 著 底 低 貯 滴 寂 摘 笛 跡 蹟 積 籍 績 賊 適 敵 赤 的 甸 殿 專 轉 錢 田 傳 典 展 戰 全 前 電 竊 折 絶 切 節 漸 占 點 店 蝶 接 旌 晶 楨 汀 珽 禎 鄭 鼎 偵 呈 艇 訂 井 亭 廷 征 淨 貞 頂 丁 整 靜 政 程 精 停 情 定 庭 正 劑 堤 諸 齊 帝 制 提 濟 祭 製 除 際 第 題 弟 曺 祚 趙 彫 措 釣 弔 燥 兆 照 租 條 潮 組 助 早 造 鳥 操 調 朝 祖 族 足 存 尊 拙 卒 琮 綜 縱 從 鍾 宗 終 種 佐 坐 座 左 罪 疇 駐 舟 奏 宙 柱 株 洲 珠 鑄 周 朱 酒 走 州 週 晝 注 主 住 竹 埈 峻 晙 浚 濬 駿 准 俊 遵 準 仲 衆 重 中 卽 贈 憎 曾 症 蒸 證 增 址 芝 旨 脂 只 遲 之 枝 池 持 智 誌 志 指 支 至 止 知 地 紙 稙 稷 織 職 直 晋 秦 塵 津 診 振 辰 鎭 陳 震 珍 盡 陣 眞 進 窒 姪 疾 秩 質 輯 執 集 懲 徵
 遮 且 借 此 差 次 捉 錯 着 燦 璨 瓚 鑽 餐 贊 讚 刹 札 察 斬 慘 慙 參 敞 昶 彰 滄 暢 倉 昌 蒼 創 唱 窓 埰 蔡 采 債 彩 菜 採 策 冊 責 悽 妻 處 陟 隻 斥 尺 戚 拓 釧 薦 淺 賤 踐 遷 泉 千 天 川 喆 澈 撤 哲 徹 鐵 瞻 尖 添 諜 妾 晴 廳 聽 請 淸 靑 締 替 逮 遞 滯 體 楚 哨 焦 抄 秒 礎 肖 超 招 初 草 蜀 燭 促 觸 村 寸 聰 總 銃 崔 催 最 楸 鄒 趨 抽 醜 追 推 秋 蹴 軸 丑 逐 畜 縮 築 蓄 祝 椿 春 出 沖 衷 衝 忠 蟲 充 聚 炊 臭 吹 醉 就 趣 取 側 測 層 峙 雉 値 恥 稚 治 置 齒 致 則 親 漆 七 枕 沈 浸 寢 針 侵 稱
 快
 墮 妥 他 打 琢 託 托 濁 濯 卓 灘 誕 彈 歎 炭 奪 脫 耽 貪 探 塔 湯 兌 台 胎 颱 怠 殆 泰 態 太 澤 擇 宅 兔 吐 討 土 痛 統 通 退 透 投 鬪 特
 坡 把 播 罷 頗 派 波 破 阪 販 版 判 板 八 霸 貝 敗 彭 扁 遍 偏 片 編 篇 便 坪 評 平 幣 蔽 廢 弊 肺 閉 葡 鮑 怖 抛 鋪 抱 飽 捕 浦 胞 包 布 砲 幅 爆 暴 杓 漂 標 票 表 品 楓 豊 風 彼 皮 被 疲 避 弼 匹 畢 必 筆
 何 荷 賀 河 下 夏 虐 鶴 學 邯 翰 旱 汗 恨 閑 限 寒 漢 韓 割 艦 咸 含 陷 合 亢 沆 巷 恒 項 抗 港 航 亥 奚 該 解 害 海 核 杏 幸 行 享 響 鄕 香 向 虛 許 軒 獻 憲 險 驗 爀 赫 革 峴 炫 鉉 弦 絃 縣 懸 玄 顯 賢 現 穴 血 嫌 陜 峽 脅 協 瀅 炯 瑩 邢 馨 型 亨 螢 衡 刑 形 兄 兮 慧 惠 壕 扈 昊 晧 澔 皓 祜 鎬 濠 乎 互 毫 浩 胡 虎 豪 呼 好 戶 護 湖 號 酷 惑 或 昏 魂 婚 混 忽 泓 弘 鴻 洪 紅 嬅 樺 靴 禾 禍 華 貨 化 和 畫 花 話 火 擴 穫 確 桓 煥 幻 丸 換 還 歡 環 患 滑 活 晃 滉 皇 荒 況 黃 檜 淮 廻 悔 懷 灰 回 會 劃 獲 橫 曉 效 孝 后 喉 侯 候 厚 後 壎 熏 薰 勳 訓 毁 徽 輝 揮 烋 携 休 匈 胸 凶 黑 欽 吸 興 嬉 憙 熹 禧 羲 噫 姬 熙 稀 戲 喜 希
"""

grade3 = """佳 架 暇 假 街 加 可 價 家 歌 却 脚 閣 刻 覺 各 角 姦 刊 幹 懇 肝 干 看 簡 間 渴 鑑 敢 甘 減 監 感 甲 剛 綱 鋼 降 康 講 強 江 慨 皆 介 槪 蓋 個 改 開 客 距 居 巨 拒 據 去 擧 車 乾 件 健 建 乞 傑 劍 儉 檢 隔 擊 激 格 牽 絹 肩 遣 堅 犬 見 訣 潔 缺 決 結 兼 謙 卿 庚 竟 徑 硬 耕 頃 傾 更 鏡 驚 境 慶 經 警 景 競 輕 敬 京 癸 繫 啓 契 桂 械 溪 季 戒 系 繼 階 鷄 係 界 計 枯 顧 姑 稿 鼓 孤 庫 故 固 考 告 古 苦 高 哭 谷 穀 曲 坤 困 骨 供 恐 恭 貢 孔 攻 公 共 功 工 空 寡 誇 課 過 果 科 郭 冠 寬 慣 貫 館 管 官 觀 關 狂 鑛 廣 光 掛 塊 愧 壞 怪 矯 郊 巧 較 橋 交 敎 校 俱 懼 狗 苟 驅 龜 丘 久 拘 構 句 求 究 救 具 舊 區 球 口 九 菊 局 國 君 群 郡 軍 屈 弓 窮 宮 拳 券 勸 卷 權 厥 軌 鬼 歸 貴 叫 糾 規 菌 均 克 劇 極 僅 斤 謹 勤 筋 根 近 琴 禽 錦 禁 今 金 及 給 急 級 肯 幾 忌 旣 棄 欺 豈 飢 企 其 畿 祈 騎 奇 寄 機 紀 器 起 技 期 汽 基 己 旗 氣 記 緊 吉
 那 諾 暖 難 男 南 納 娘 乃 奈 耐 內 女 年 念 寧 奴 努 怒 農 惱 腦 能 泥
 茶 多 丹 但 旦 段 單 斷 檀 端 壇 團 短 達 淡 擔 談 畓 踏 答 唐 糖 黨 當 堂 臺 貸 帶 隊 代 對 待 大 德 塗 挑 稻 跳 倒 刀 桃 渡 途 陶 徒 盜 逃 導 島 都 到 圖 度 道 篤 毒 督 獨 讀 敦 豚 突 凍 銅 童 冬 動 同 洞 東 斗 豆 頭 屯 鈍 得 騰 燈 等 登
 羅 絡 落 樂 欄 蘭 亂 卵 濫 覽 廊 浪 郞 朗 來 冷 掠 略 諒 梁 涼 糧 兩 量 良 勵 慮 麗 旅 曆 歷 力 憐 戀 聯 蓮 鍊 連 練 劣 裂 烈 列 廉 獵 零 嶺 靈 令 領 隷 例 禮 爐 露 勞 路 老 鹿 祿 錄 綠 論 弄 賴 雷 了 僚 料 龍 屢 淚 樓 漏 累 柳 留 流 類 陸 六 倫 輪 栗 率 律 隆 陵 梨 吏 履 裏 離 利 李 理 里 隣 臨 林 立
 磨 麻 馬 幕 漠 莫 慢 漫 晩 滿 萬 末 忘 忙 罔 茫 妄 亡 望 埋 媒 梅 妹 買 賣 每 麥 脈 孟 猛 盲 盟 免 眠 綿 勉 面 滅 冥 銘 鳴 明 名 命 侮 冒 募 暮 某 慕 謀 貌 模 毛 母 睦 牧 目 木 沒 夢 蒙 卯 廟 苗 墓 妙 戊 霧 茂 貿 舞 務 武 無 墨 默 紋 聞 問 文 門 勿 物 眉 迷 尾 微 味 未 米 美 憫 敏 民 蜜 密
 泊 薄 迫 拍 博 朴 伴 叛 返 盤 般 飯 半 反 班 拔 髮 發 倣 傍 邦 芳 妨 房 訪 防 放 方 杯 培 排 輩 拜 背 配 倍 伯 百 白 煩 飜 繁 番 伐 罰 凡 犯 範 法 碧 壁 辨 辯 邊 變 別 屛 竝 丙 兵 病 補 譜 普 保 報 寶 步 卜 腹 覆 伏 複 復 福 服 本 蜂 封 峯 逢 鳳 奉 赴 付 扶 浮 符 簿 腐 賦 附 否 負 副 婦 富 府 部 夫 父 北 墳 奔 奮 紛 憤 粉 分 拂 佛 不 崩 朋 卑 妃 婢 肥 批 碑 祕 備 悲 非 飛 比 費 鼻 賓 頻 貧 聘 氷
 似 巳 捨 斯 詐 賜 司 斜 沙 祀 蛇 詞 邪 射 私 絲 辭 寺 師 舍 謝 寫 思 査 仕 史 士 使 死 社 事 四 朔 削 散 産 算 山 殺 森 三 嘗 祥 像 償 喪 尙 桑 裳 詳 霜 傷 象 常 床 想 狀 賞 商 相 上 塞 索 色 生 庶 敍 暑 誓 逝 徐 恕 緖 署 序 書 西 昔 析 惜 釋 席 石 夕 旋 禪 宣 善 船 選 仙 鮮 線 先 舌 設 說 雪 攝 涉 城 星 盛 聖 聲 誠 性 成 省 姓 勢 稅 細 歲 洗 世 召 昭 蔬 騷 燒 疏 蘇 訴 掃 笑 素 消 少 所 小 粟 屬 俗 續 束 速 損 孫 誦 訟 松 頌 送 刷 鎖 衰 囚 搜 睡 誰 遂 雖 須 垂 壽 帥 愁 殊 獸 輸 隨 需 秀 修 受 守 授 收 首 樹 手 數 水 孰 淑 熟 叔 肅 宿 循 殉 脣 巡 旬 瞬 純 順 戌 述 術 崇 濕 拾 襲 習 乘 僧 昇 承 勝 矢 侍 施 是 視 試 詩 示 始 市 時 飾 息 識 式 植 食 伸 晨 辛 愼 申 臣 信 新 神 身 實 失 室 尋 審 甚 深 心 十 雙 氏
 餓 亞 我 牙 芽 阿 雅 兒 岳 惡 雁 岸 顔 眼 案 安 謁 巖 暗 押 壓 殃 仰 央 涯 哀 愛 厄 額 液 也 耶 夜 野 躍 若 約 弱 藥 楊 壤 揚 讓 樣 羊 養 洋 陽 於 御 漁 魚 語 憶 抑 億 焉 言 嚴 業 予 余 汝 輿 與 如 餘 亦 役 疫 譯 驛 域 易 逆 宴 沿 燕 軟 延 燃 緣 鉛 演 煙 硏 然 閱 悅 熱 染 炎 鹽 葉 泳 詠 影 映 營 迎 榮 永 英 銳 譽 豫 藝 傲 吾 嗚 娛 汚 悟 烏 誤 午 五 獄 玉 屋 溫 擁 翁 臥 瓦 緩 完 曰 往 王 畏 外 搖 腰 遙 謠 曜 要 慾 欲 辱 浴 庸 容 勇 用 于 又 尤 偶 宇 愚 憂 羽 優 遇 郵 牛 友 雨 右 云 韻 雲 運 雄 怨 援 源 員 圓 原 院 願 元 園 遠 越 月 緯 違 僞 胃 謂 危 圍 委 威 慰 爲 衛 位 偉 唯 惟 愈 酉 幼 幽 悠 柔 猶 維 裕 誘 乳 儒 遊 遺 油 由 有 肉 育 閏 潤 隱 恩 銀 乙 吟 淫 陰 音 飮 泣 邑 凝 應 宜 矣 依 儀 疑 義 議 意 衣 醫 夷 而 已 異 移 耳 以 二 翼 益 姻 寅 忍 仁 印 引 認 因 人 逸 一 日 壬 賃 任 入
 恣 玆 刺 慈 紫 姉 姿 資 者 子 字 自 爵 酌 作 昨 殘 暫 潛 雜 墻 丈 掌 粧 臟 莊 葬 藏 壯 帳 張 腸 裝 獎 將 障 章 場 長 哉 宰 栽 裁 載 再 災 材 財 在 才 爭 抵 著 底 低 貯 滴 寂 摘 笛 跡 蹟 積 籍 績 賊 適 敵 赤 的 殿 專 轉 錢 田 傳 典 展 戰 全 前 電 竊 折 絶 切 節 漸 占 點 店 蝶 接 訂 井 亭 廷 征 淨 貞 頂 丁 整 靜 政 程 精 停 情 定 庭 正 堤 諸 齊 帝 制 提 濟 祭 製 除 際 第 題 弟 弔 燥 兆 照 租 條 潮 組 助 早 造 鳥 操 調 朝 祖 族 足 存 尊 拙 卒 縱 從 鍾 宗 終 種 佐 坐 座 左 罪 舟 奏 宙 柱 株 洲 珠 鑄 周 朱 酒 走 州 週 晝 注 主 住 竹 俊 遵 準 仲 衆 重 中 卽 贈 憎 曾 症 蒸 證 增 只 遲 之 枝 池 持 智 誌 志 指 支 至 止 知 地 紙 織 職 直 振 辰 鎭 陳 震 珍 盡 陣 眞 進 姪 疾 秩 質 執 集 懲 徵
 且 借 此 差 次 捉 錯 着 贊 讚 察 慘 慙 參 暢 倉 昌 蒼 創 唱 窓 債 彩 菜 採 策 冊 責 妻 處 斥 尺 戚 拓 薦 淺 賤 踐 遷 泉 千 天 川 哲 徹 鐵 尖 添 妾 晴 廳 聽 請 淸 靑 替 逮 遞 滯 體 抄 秒 礎 肖 超 招 初 草 燭 促 觸 村 寸 聰 總 銃 催 最 抽 醜 追 推 秋 丑 逐 畜 縮 築 蓄 祝 春 出 衝 忠 蟲 充 臭 吹 醉 就 趣 取 側 測 層 値 恥 稚 治 置 齒 致 則 親 漆 七 枕 沈 浸 寢 針 侵 稱
 快
 墮 妥 他 打 托 濁 濯 卓 誕 彈 歎 炭 奪 脫 貪 探 塔 湯 怠 殆 泰 態 太 澤 擇 宅 兔 吐 討 土 痛 統 通 退 透 投 鬪 特
 把 播 罷 頗 派 波 破 販 版 判 板 八 貝 敗 遍 偏 片 編 篇 便 評 平 幣 蔽 廢 弊 肺 閉 抱 飽 捕 浦 胞 包 布 砲 幅 爆 暴 漂 標 票 表 品 楓 豊 風 彼 皮 被 疲 避 匹 畢 必 筆
 何 荷 賀 河 下 夏 鶴 學 旱 汗 恨 閑 限 寒 漢 韓 割 咸 含 陷 合 巷 恒 項 抗 港 航 亥 奚 該 解 害 海 核 幸 行 享 響 鄕 香 向 虛 許 軒 獻 憲 險 驗 革 絃 縣 懸 玄 顯 賢 現 穴 血 嫌 脅 協 亨 螢 衡 刑 形 兄 兮 慧 惠 乎 互 毫 浩 胡 虎 豪 呼 好 戶 護 湖 號 惑 或 昏 魂 婚 混 忽 弘 鴻 洪 紅 禾 禍 華 貨 化 和 畫 花 話 火 擴 穫 確 丸 換 還 歡 環 患 活 皇 荒 況 黃 悔 懷 灰 回 會 劃 獲 橫 曉 效 孝 侯 候 厚 後 訓 毁 輝 揮 携 休 胸 凶 黑 吸 興 稀 戲 喜 希 
"""

grade3II = """佳 架 暇 假 街 加 可 價 家 歌 脚 閣 刻 覺 各 角 刊 幹 懇 肝 干 看 簡 間 鑑 敢 甘 減 監 感 甲 剛 綱 鋼 降 康 講 強 江 介 槪 蓋 個 改 開 客 距 居 巨 拒 據 去 擧 車 乾 件 健 建 傑 劍 儉 檢 隔 擊 激 格 堅 犬 見 訣 潔 缺 決 結 兼 謙 徑 硬 耕 頃 傾 更 鏡 驚 境 慶 經 警 景 競 輕 敬 京 啓 契 桂 械 溪 季 戒 系 繼 階 鷄 係 界 計 姑 稿 鼓 孤 庫 故 固 考 告 古 苦 高 哭 谷 穀 曲 困 骨 供 恐 恭 貢 孔 攻 公 共 功 工 空 寡 誇 課 過 果 科 冠 寬 慣 貫 館 管 官 觀 關 狂 鑛 廣 光 壞 怪 巧 較 橋 交 敎 校 丘 久 拘 構 句 求 究 救 具 舊 區 球 口 九 菊 局 國 君 群 郡 軍 屈 弓 窮 宮 拳 券 勸 卷 權 鬼 歸 貴 規 菌 均 克 劇 極 勤 筋 根 近 琴 禽 錦 禁 今 金 及 給 急 級 企 其 畿 祈 騎 奇 寄 機 紀 器 起 技 期 汽 基 己 旗 氣 記 緊 吉
諾 暖 難 男 南 納 娘 耐 內 女 年 念 寧 奴 努 怒 農 腦 能 泥
茶 多 丹 但 旦 段 單 斷 檀 端 壇 團 短 達 淡 擔 談 踏 答 唐 糖 黨 當 堂 臺 貸 帶 隊 代 對 待 大 德 倒 刀 桃 渡 途 陶 徒 盜 逃 導 島 都 到 圖 度 道 毒 督 獨 讀 突 凍 銅 童 冬 動 同 洞 東 斗 豆 頭 得 燈 等 登
羅 絡 落 樂 欄 蘭 亂 卵 覽 廊 浪 郞 朗 來 冷 略 梁 涼 糧 兩 量 良 勵 慮 麗 旅 曆 歷 力 戀 聯 蓮 鍊 連 練 裂 烈 列 嶺 靈 令 領 例 禮 爐 露 勞 路 老 祿 錄 綠 論 弄 賴 雷 料 龍 樓 漏 累 柳 留 流 類 陸 六 倫 輪 栗 率 律 隆 陵 吏 履 裏 離 利 李 理 里 臨 林 立
磨 麻 馬 幕 漠 莫 晩 滿 萬 末 妄 亡 望 媒 梅 妹 買 賣 每 麥 脈 孟 猛 盲 盟 免 眠 綿 勉 面 滅 銘 鳴 明 名 命 慕 謀 貌 模 毛 母 睦 牧 目 木 沒 夢 蒙 墓 妙 茂 貿 舞 務 武 無 墨 默 紋 聞 問 文 門 勿 物 尾 微 味 未 米 美 民 密
薄 迫 拍 博 朴 盤 般 飯 半 反 班 拔 髮 發 芳 妨 房 訪 防 放 方 培 排 輩 拜 背 配 倍 伯 百 白 繁 番 伐 罰 凡 犯 範 法 碧 壁 辯 邊 變 別 丙 兵 病 補 譜 普 保 報 寶 步 腹 覆 伏 複 復 福 服 本 封 峯 逢 鳳 奉 付 扶 浮 符 簿 腐 賦 附 否 負 副 婦 富 府 部 夫 父 北 奔 奮 紛 憤 粉 分 拂 佛 不 卑 妃 婢 肥 批 碑 祕 備 悲 非 飛 比 費 鼻 貧 氷
司 斜 沙 祀 蛇 詞 邪 射 私 絲 辭 寺 師 舍 謝 寫 思 査 仕 史 士 使 死 社 事 四 削 散 産 算 山 殺 森 三 像 償 喪 尙 桑 裳 詳 霜 傷 象 常 床 想 狀 賞 商 相 上 塞 索 色 生 徐 恕 緖 署 序 書 西 惜 釋 席 石 夕 旋 禪 宣 善 船 選 仙 鮮 線 先 舌 設 說 雪 城 星 盛 聖 聲 誠 性 成 省 姓 勢 稅 細 歲 洗 世 燒 疏 蘇 訴 掃 笑 素 消 少 所 小 屬 俗 續 束 速 損 孫 訟 松 頌 送 刷 鎖 衰 垂 壽 帥 愁 殊 獸 輸 隨 需 秀 修 受 守 授 收 首 樹 手 數 水 淑 熟 叔 肅 宿 巡 旬 瞬 純 順 述 術 崇 濕 拾 襲 習 乘 僧 昇 承 勝 侍 施 是 視 試 詩 示 始 市 時 飾 息 識 式 植 食 愼 申 臣 信 新 神 身 實 失 室 審 甚 深 心 十 雙 氏
亞 我 牙 芽 阿 雅 兒 惡 岸 顔 眼 案 安 巖 暗 壓 仰 央 哀 愛 額 液 夜 野 若 約 弱 藥 壤 揚 讓 樣 羊 養 洋 陽 御 漁 魚 語 憶 抑 億 言 嚴 業 與 如 餘 亦 役 疫 譯 驛 域 易 逆 宴 沿 燕 軟 延 燃 緣 鉛 演 煙 硏 然 悅 熱 染 炎 鹽 葉 影 映 營 迎 榮 永 英 譽 豫 藝 悟 烏 誤 午 五 獄 玉 屋 溫 瓦 緩 完 往 王 外 謠 曜 要 慾 欲 辱 浴 容 勇 用 偶 宇 愚 憂 羽 優 遇 郵 牛 友 雨 右 韻 雲 運 雄 怨 援 源 員 圓 原 院 願 元 園 遠 越 月 僞 胃 謂 危 圍 委 威 慰 爲 衛 位 偉 幼 幽 悠 柔 猶 維 裕 誘 乳 儒 遊 遺 油 由 有 肉 育 潤 隱 恩 銀 乙 淫 陰 音 飮 邑 應 依 儀 疑 義 議 意 衣 醫 已 異 移 耳 以 二 翼 益 忍 仁 印 引 認 因 人 逸 一 日 壬 賃 任 入
刺 慈 紫 姉 姿 資 者 子 字 自 作 昨 殘 暫 潛 雜 丈 掌 粧 臟 莊 葬 藏 壯 帳 張 腸 裝 獎 將 障 章 場 長 栽 裁 載 再 災 材 財 在 才 爭 抵 著 底 低 貯 寂 摘 笛 跡 蹟 積 籍 績 賊 適 敵 赤 的 殿 專 轉 錢 田 傳 典 展 戰 全 前 電 折 絶 切 節 漸 占 點 店 接 井 亭 廷 征 淨 貞 頂 丁 整 靜 政 程 精 停 情 定 庭 正 諸 齊 帝 制 提 濟 祭 製 除 際 第 題 弟 兆 照 租 條 潮 組 助 早 造 鳥 操 調 朝 祖 族 足 存 尊 卒 縱 從 鍾 宗 終 種 坐 座 左 罪 奏 宙 柱 株 洲 珠 鑄 周 朱 酒 走 州 週 晝 注 主 住 竹 準 仲 衆 重 中 卽 憎 曾 症 蒸 證 增 之 枝 池 持 智 誌 志 指 支 至 止 知 地 紙 織 職 直 振 辰 鎭 陳 震 珍 盡 陣 眞 進 疾 秩 質 執 集 徵
借 此 差 次 錯 着 贊 讚 察 參 倉 昌 蒼 創 唱 窓 債 彩 菜 採 策 冊 責 妻 處 尺 戚 拓 淺 賤 踐 遷 泉 千 天 川 哲 徹 鐵 廳 聽 請 淸 靑 滯 體 礎 肖 超 招 初 草 促 觸 村 寸 總 銃 催 最 追 推 秋 畜 縮 築 蓄 祝 春 出 衝 忠 蟲 充 吹 醉 就 趣 取 側 測 層 値 恥 稚 治 置 齒 致 則 親 漆 七 沈 浸 寢 針 侵 稱
快
他 打 卓 彈 歎 炭 奪 脫 探 塔 湯 殆 泰 態 太 澤 擇 宅 兔 吐 討 土 痛 統 通 退 透 投 鬪 特
派 波 破 版 判 板 八 敗 偏 片 編 篇 便 評 平 廢 弊 肺 閉 捕 浦 胞 包 布 砲 爆 暴 標 票 表 品 楓 豊 風 彼 皮 被 疲 避 畢 必 筆
何 荷 賀 河 下 夏 鶴 學 汗 恨 閑 限 寒 漢 韓 割 含 陷 合 恒 項 抗 港 航 解 害 海 核 幸 行 響 鄕 香 向 虛 許 獻 憲 險 驗 革 懸 玄 顯 賢 現 穴 血 脅 協 衡 刑 形 兄 慧 惠 浩 胡 虎 豪 呼 好 戶 護 湖 號 惑 或 魂 婚 混 忽 洪 紅 禍 華 貨 化 和 畫 花 話 火 確 換 還 歡 環 患 活 皇 荒 況 黃 悔 懷 灰 回 會 劃 獲 橫 效 孝 候 厚 後 訓 揮 休 胸 凶 黑 吸 興 稀 戲 喜 希 
"""

grade4 = """暇 假 街 加 可 價 家 歌 刻 覺 各 角 干 看 簡 間 敢 甘 減 監 感 甲 降 康 講 強 江 個 改 開 客 居 巨 拒 據 去 擧 車 件 健 建 傑 儉 檢 擊 激 格 堅 犬 見 潔 缺 決 結 傾 更 鏡 驚 境 慶 經 警 景 競 輕 敬 京 季 戒 系 繼 階 鷄 係 界 計 孤 庫 故 固 考 告 古 苦 高 穀 曲 困 骨 孔 攻 公 共 功 工 空 課 過 果 科 管 官 觀 關 鑛 廣 光 橋 交 敎 校 構 句 求 究 救 具 舊 區 球 口 九 局 國 君 群 郡 軍 屈 窮 宮 券 勸 卷 權 歸 貴 規 均 劇 極 勤 筋 根 近 禁 今 金 給 急 級 奇 寄 機 紀 器 起 技 期 汽 基 己 旗 氣 記 吉
 暖 難 男 南 納 內 女 年 念 努 怒 農 能
 多 段 單 斷 檀 端 壇 團 短 達 擔 談 答 黨 當 堂 帶 隊 代 對 待 大 德 徒 盜 逃 導 島 都 到 圖 度 道 毒 督 獨 讀 銅 童 冬 動 同 洞 東 斗 豆 頭 得 燈 等 登
 羅 落 樂 亂 卵 覽 朗 來 冷 略 糧 兩 量 良 慮 麗 旅 歷 力 連 練 烈 列 令 領 例 禮 勞 路 老 錄 綠 論 料 龍 柳 留 流 類 陸 六 輪 律 離 利 李 理 里 林 立
 馬 滿 萬 末 亡 望 妹 買 賣 每 脈 勉 面 鳴 明 名 命 模 毛 母 牧 目 木 墓 妙 舞 務 武 無 聞 問 文 門 物 味 未 米 美 民 密
 拍 博 朴 半 反 班 髮 發 妨 房 訪 防 放 方 拜 背 配 倍 百 白 番 伐 罰 犯 範 法 壁 辯 邊 變 別 兵 病 普 保 報 寶 步 伏 複 復 福 服 本 奉 否 負 副 婦 富 府 部 夫 父 北 憤 粉 分 佛 不 批 碑 祕 備 悲 非 飛 比 費 鼻 貧 氷
 射 私 絲 辭 寺 師 舍 謝 寫 思 査 仕 史 士 使 死 社 事 四 散 産 算 山 殺 三 傷 象 常 床 想 狀 賞 商 相 上 色 生 序 書 西 席 石 夕 宣 善 船 選 仙 鮮 線 先 舌 設 說 雪 城 星 盛 聖 聲 誠 性 成 省 姓 勢 稅 細 歲 洗 世 掃 笑 素 消 少 所 小 屬 俗 續 束 速 損 孫 松 頌 送 秀 修 受 守 授 收 首 樹 手 數 水 叔 肅 宿 純 順 術 崇 習 承 勝 施 是 視 試 詩 示 始 市 時 息 識 式 植 食 申 臣 信 新 神 身 實 失 室 深 心 十 氏
 兒 惡 眼 案 安 暗 壓 愛 額 液 夜 野 約 弱 藥 樣 羊 養 洋 陽 漁 魚 語 億 言 嚴 業 與 如 餘 域 易 逆 延 燃 緣 鉛 演 煙 硏 然 熱 葉 映 營 迎 榮 永 英 豫 藝 誤 午 五 玉 屋 溫 完 往 王 外 謠 曜 要 浴 容 勇 用 優 遇 郵 牛 友 雨 右 雲 運 雄 怨 援 源 員 圓 原 院 願 元 園 遠 月 危 圍 委 威 慰 爲 衛 位 偉 乳 儒 遊 遺 油 由 有 肉 育 隱 恩 銀 陰 音 飮 邑 應 依 儀 疑 義 議 意 衣 醫 異 移 耳 以 二 益 仁 印 引 認 因 人 一 日 任 入
 姉 姿 資 者 子 字 自 作 昨 殘 雜 壯 帳 張 腸 裝 獎 將 障 章 場 長 再 災 材 財 在 才 爭 底 低 貯 積 籍 績 賊 適 敵 赤 的 專 轉 錢 田 傳 典 展 戰 全 前 電 折 絶 切 節 占 點 店 接 丁 整 靜 政 程 精 停 情 定 庭 正 帝 制 提 濟 祭 製 除 際 第 題 弟 條 潮 組 助 早 造 鳥 操 調 朝 祖 族 足 存 尊 卒 從 鍾 宗 終 種 座 左 罪 周 朱 酒 走 州 週 晝 注 主 住 竹 準 衆 重 中 證 增 持 智 誌 志 指 支 至 止 知 地 紙 織 職 直 珍 盡 陣 眞 進 質 集
 差 次 着 讚 察 參 創 唱 窓 採 冊 責 處 泉 千 天 川 鐵 廳 聽 請 淸 靑 體 招 初 草 村 寸 總 銃 最 推 秋 縮 築 蓄 祝 春 出 忠 蟲 充 就 趣 取 測 層 治 置 齒 致 則 親 七 寢 針 侵 稱
 快
 他 打 卓 彈 歎 炭 脫 探 態 太 擇 宅 討 土 痛 統 通 退 投 鬪 特
 派 波 破 判 板 八 敗 篇 便 評 平 閉 胞 包 布 砲 爆 暴 標 票 表 品 豊 風 疲 避 必 筆
 河 下 夏 學 恨 閑 限 寒 漢 韓 合 抗 港 航 解 害 海 核 幸 行 鄕 香 向 虛 許 憲 險 驗 革 顯 賢 現 血 協 刑 形 兄 惠 呼 好 戶 護 湖 號 或 婚 混 紅 華 貨 化 和 畫 花 話 火 確 歡 環 患 活 況 黃 灰 回 會 效 孝 候 厚 後 訓 揮 休 凶 黑 吸 興 喜 希
"""

grade4II = """假 街 加 可 價 家 歌 各 角 間 減 監 感 康 講 強 江 個 改 開 客 去 擧 車 件 健 建 檢 格 見 潔 缺 決 結 境 慶 經 警 景 競 輕 敬 京 係 界 計 故 固 考 告 古 苦 高 曲 公 共 功 工 空 課 過 果 科 官 觀 關 廣 光 橋 交 敎 校 句 求 究 救 具 舊 區 球 口 九 局 國 郡 軍 宮 權 貴 規 極 根 近 禁 今 金 給 急 級 器 起 技 期 汽 基 己 旗 氣 記 吉
 暖 難 男 南 內 女 年 念 努 怒 農 能
 多 單 斷 檀 端 壇 團 短 達 擔 談 答 黨 當 堂 帶 隊 代 對 待 大 德 導 島 都 到 圖 度 道 毒 督 獨 讀 銅 童 冬 動 同 洞 東 斗 豆 頭 得 燈 等 登
 羅 落 樂 朗 來 冷 兩 量 良 麗 旅 歷 力 連 練 列 令 領 例 禮 勞 路 老 錄 綠 論 料 留 流 類 陸 六 律 利 李 理 里 林 立
 馬 滿 萬 末 亡 望 買 賣 每 脈 面 明 名 命 毛 母 牧 目 木 務 武 無 聞 問 文 門 物 味 未 米 美 民 密
 博 朴 半 反 班 發 房 訪 防 放 方 拜 背 配 倍 百 白 番 伐 罰 法 壁 邊 變 別 兵 病 保 報 寶 步 復 福 服 本 奉 副 婦 富 府 部 夫 父 北 分 佛 不 備 悲 非 飛 比 費 鼻 貧 氷
 寺 師 舍 謝 寫 思 査 仕 史 士 使 死 社 事 四 産 算 山 殺 三 常 床 想 狀 賞 商 相 上 色 生 序 書 西 席 石 夕 善 船 選 仙 鮮 線 先 設 說 雪 城 星 盛 聖 聲 誠 性 成 省 姓 勢 稅 細 歲 洗 世 掃 笑 素 消 少 所 小 俗 續 束 速 孫 送 修 受 守 授 收 首 樹 手 數 水 宿 純 順 術 習 承 勝 施 是 視 試 詩 示 始 市 時 息 識 式 植 食 申 臣 信 新 神 身 實 失 室 深 心 十
 兒 惡 眼 案 安 暗 壓 愛 液 夜 野 約 弱 藥 羊 養 洋 陽 漁 魚 語 億 言 業 如 餘 逆 演 煙 硏 然 熱 葉 榮 永 英 藝 誤 午 五 玉 屋 溫 完 往 王 外 謠 曜 要 浴 容 勇 用 牛 友 雨 右 雲 運 雄 員 圓 原 院 願 元 園 遠 月 爲 衛 位 偉 油 由 有 肉 育 恩 銀 陰 音 飮 邑 應 義 議 意 衣 醫 移 耳 以 二 益 印 引 認 因 人 一 日 任 入
 者 子 字 自 作 昨 將 障 章 場 長 再 災 材 財 在 才 爭 低 貯 敵 赤 的 田 傳 典 展 戰 全 前 電 絶 切 節 店 接 政 程 精 停 情 定 庭 正 制 提 濟 祭 製 除 際 第 題 弟 助 早 造 鳥 操 調 朝 祖 族 足 尊 卒 宗 終 種 左 罪 走 州 週 晝 注 主 住 竹 準 衆 重 中 增 志 指 支 至 止 知 地 紙 職 直 眞 進 質 集
 次 着 察 參 創 唱 窓 責 處 千 天 川 鐵 請 淸 靑 體 初 草 村 寸 總 銃 最 秋 築 蓄 祝 春 出 忠 蟲 充 取 測 治 置 齒 致 則 親 七 侵
 快
 他 打 卓 炭 態 太 宅 土 統 通 退 特
 波 破 板 八 敗 便 平 包 布 砲 暴 票 表 品 豊 風 必 筆
 河 下 夏 學 限 寒 漢 韓 合 港 航 解 害 海 幸 行 鄕 香 向 虛 許 驗 賢 現 血 協 形 兄 惠 呼 好 戶 護 湖 號 貨 化 和 畫 花 話 火 確 患 活 黃 回 會 效 孝 後 訓 休 凶 黑 吸 興 希 
"""

grade5 = """加 可 價 家 歌 各 角 間 感 強 江 改 開 客 去 擧 車 件 健 建 格 見 決 結 景 競 輕 敬 京 界 計 固 考 告 古 苦 高 曲 公 共 功 工 空 課 過 果 科 觀 關 廣 光 橋 交 敎 校 救 具 舊 區 球 口 九 局 國 郡 軍 貴 規 根 近 今 金 給 急 級 技 期 汽 基 己 旗 氣 記 吉
 男 南 內 女 年 念 農 能
 多 壇 團 短 談 答 當 堂 代 對 待 大 德 島 都 到 圖 度 道 獨 讀 童 冬 動 同 洞 東 頭 等 登
 落 樂 朗 來 冷 量 良 旅 歷 力 練 令 領 例 禮 勞 路 老 綠 料 流 類 陸 六 利 李 理 里 林 立
 馬 萬 末 亡 望 買 賣 每 面 明 名 命 母 目 木 無 聞 問 文 門 物 米 美 民
 朴 半 反 班 發 放 方 倍 百 白 番 法 變 別 兵 病 福 服 本 奉 部 夫 父 北 分 不 比 費 鼻 氷
 寫 思 査 仕 史 士 使 死 社 事 四 産 算 山 三 賞 商 相 上 色 生 序 書 西 席 石 夕 善 船 選 仙 鮮 線 先 說 雪 性 成 省 姓 歲 洗 世 消 少 所 小 束 速 孫 首 樹 手 數 水 宿 順 術 習 勝 示 始 市 時 識 式 植 食 臣 信 新 神 身 實 失 室 心 十
 兒 惡 案 安 愛 夜 野 約 弱 藥 養 洋 陽 漁 魚 語 億 言 業 然 熱 葉 永 英 午 五 屋 溫 完 王 外 曜 要 浴 勇 用 牛 友 雨 右 雲 運 雄 原 院 願 元 園 遠 月 位 偉 油 由 有 育 銀 音 飮 邑 意 衣 醫 耳 以 二 因 人 一 日 任 入
 者 子 字 自 作 昨 章 場 長 再 災 材 財 在 才 爭 貯 赤 的 傳 典 展 戰 全 前 電 切 節 店 停 情 定 庭 正 第 題 弟 操 調 朝 祖 族 足 卒 終 種 左 罪 州 週 晝 注 主 住 重 中 止 知 地 紙 直 質 集
 着 參 唱 窓 責 千 天 川 鐵 淸 靑 體 初 草 村 寸 最 秋 祝 春 出 充 致 則 親 七
 他 打 卓 炭 太 宅 土 通 特
 板 八 敗 便 平 表 品 風 必 筆
 河 下 夏 學 寒 漢 韓 合 害 海 幸 行 向 許 現 形 兄 湖 號 化 和 畫 花 話 火 患 活 黃 會 效 孝 後 訓 休 凶 黑 
"""

grade5II = """價 家 歌 各 角 間 感 強 江 開 客 車 格 見 決 結 敬 京 界 計 告 古 苦 高 公 共 功 工 空 課 過 果 科 觀 關 廣 光 交 敎 校 具 舊 區 球 口 九 局 國 郡 軍 根 近 今 金 急 級 基 己 旗 氣 記
男 南 內 女 年 念 農 能
多 團 短 答 當 堂 代 對 待 大 德 到 圖 度 道 獨 讀 童 冬 動 同 洞 東 頭 等 登
樂 朗 來 良 旅 歷 力 練 例 禮 勞 路 老 綠 流 類 陸 六 利 李 理 里 林 立
萬 望 每 面 明 名 命 母 目 木 聞 問 文 門 物 米 美 民
朴 半 反 班 發 放 方 百 白 番 法 變 別 兵 病 福 服 本 奉 部 夫 父 北 分 不
仕 史 士 使 死 社 事 四 産 算 山 三 商 相 上 色 生 書 西 席 石 夕 仙 鮮 線 先 說 雪 性 成 省 姓 歲 洗 世 消 少 所 小 束 速 孫 首 樹 手 數 水 宿 順 術 習 勝 始 市 時 識 式 植 食 臣 信 新 神 身 實 失 室 心 十
兒 惡 安 愛 夜 野 約 弱 藥 養 洋 陽 語 言 業 然 永 英 午 五 溫 王 外 要 勇 用 友 雨 右 雲 運 元 園 遠 月 偉 油 由 有 育 銀 音 飮 邑 意 衣 醫 以 二 人 一 日 任 入
者 子 字 自 作 昨 章 場 長 材 財 在 才 的 傳 典 展 戰 全 前 電 切 節 店 情 定 庭 正 第 題 弟 調 朝 祖 族 足 卒 種 左 州 週 晝 注 主 住 重 中 知 地 紙 直 質 集
着 參 窓 責 千 天 川 淸 靑 體 草 村 寸 秋 春 出 充 親 七
太 宅 土 通 特
八 便 平 表 品 風 必 筆
下 夏 學 漢 韓 合 害 海 幸 行 向 現 形 兄 號 化 和 畫 花 話 火 活 黃 會 效 孝 後 訓 休 凶
"""

grade6 = """* 글꼴을 바꾸면 漢字 모양이 바뀔 수 있습니다.
* 본 문서는 글 2007에서 작성되었습니다.

6級 읽기配定漢字 300字

ㄱ 家 歌 各 角 間 感 強 江 開 車 京 界 計 古 苦 高 公 共 功 工 空 果 科 光 交 敎 校 區 球 口 九 國 郡 軍 根 近 今 金 急 級 旗 氣 記
ㄴ 男 南 內 女 年 農
ㄷ 多 短 答 堂 代 對 待 大 圖 度 道 讀 童 冬 動 同 洞 東 頭 等 登
ㄹ 樂 來 力 例 禮 路 老 綠 六 利 李 理 里 林 立
ㅁ 萬 每 面 明 名 命 母 目 木 聞 問 文 門 物 米 美 民
ㅂ 朴 半 反 班 發 放 方 百 白 番 別 病 服 本 部 夫 父 北 分 不
ㅅ 使 死 社 事 四 算 山 三 上 色 生 書 西 席 石 夕 線 先 雪 成 省 姓 世 消 少 所 小 速 孫 樹 手 數 水 術 習 勝 始 市 時 式 植 食 信 新 神 身 失 室 心 十
ㅇ 安 愛 夜 野 弱 藥 洋 陽 語 言 業 然 永 英 午 五 溫 王 外 勇 用 右 運 園 遠 月 油 由 有 育 銀 音 飮 邑 意 衣 醫 二 人 一 日 入
ㅈ 者 子 字 自 作 昨 章 場 長 在 才 戰 全 前 電 定 庭 正 第 題 弟 朝 祖 族 足 左 晝 注 主 住 重 中 地 紙 直 集
ㅊ 窓 千 天 川 淸 靑 體 草 村 寸 秋 春 出 親 七
ㅌ 太 土 通 特
ㅍ 八 便 平 表 風
ㅎ 下 夏 學 漢 韓 合 海 幸 行 向 現 形 兄 號 和 畫 花 話 火 活 黃 會 孝 後 訓 休
"""


grade6II = """家 歌 各 角 間 江 車 界 計 高 公 共 功 工 空 果 科 光 敎 校 球 口 九 國 軍 今 金 急 旗 氣 記
 男 南 內 女 年 農
 短 答 堂 代 對 大 圖 道 讀 童 冬 動 同 洞 東 等 登
 樂 來 力 老 六 利 理 里 林 立
 萬 每 面 明 名 命 母 木 聞 問 文 門 物 民
 半 反 班 發 放 方 百 白 部 夫 父 北 分 不
 社 事 四 算 山 三 上 色 生 書 西 夕 線 先 雪 成 省 姓 世 消 少 所 小 手 數 水 術 始 市 時 植 食 信 新 神 身 室 心 十
 安 弱 藥 語 業 然 午 五 王 外 勇 用 右 運 月 有 育 音 飮 邑 意 二 人 一 日 入
 子 字 自 作 昨 場 長 才 戰 全 前 電 庭 正 第 題 弟 祖 足 左 注 主 住 重 中 地 紙 直 集
 窓 千 天 川 淸 靑 體 草 村 寸 秋 春 出 七
 土
 八 便 平 表 風
 下 夏 學 漢 韓 海 幸 現 形 兄 和 花 話 火 活 會 孝 後 休
"""


grade7 = """家 歌 間 江 車 工 空 敎 校 口 九 國 軍 金 旗 氣 記
 男 南 內 女 年 農
 答 大 道 冬 動 同 洞 東 登
 來 力 老 六 里 林 立
 萬 每 面 名 命 母 木 問 文 門 物 民
 方 百 白 夫 父 北 不
 事 四 算 山 三 上 色 生 西 夕 先 姓 世 少 所 小 手 數 水 市 時 植 食 室 心 十
 安 語 然 午 五 王 外 右 月 有 育 邑 二 人 一 日 入
 子 字 自 場 長 全 前 電 正 弟 祖 足 左 主 住 重 中 地 紙 直
 千 天 川 靑 草 村 寸 秋 春 出 七
 土
 八 便 平
 下 夏 學 漢 韓 海 兄 花 話 火 活 孝 後 休 
"""

grade7II = """家 間 江 車 工 空 敎 校 九 國 軍 金 氣 記
 男 南 內 女 年 農
 答 大 道 動 東
 力 六 立
 萬 每 名 母 木 門 物 民
 方 白 父 北 不
 事 四 山 三 上 生 西 先 姓 世 小 手 水 市 時 食 室 十
 安 午 五 王 外 右 月 二 人 一 日
 子 自 場 長 全 前 電 正 弟 足 左 中 直
 靑 寸 七
 土
 八 平
 下 學 漢 韓 海 兄 話 火 活 孝 後
"""

grade8 = """敎 校 九 國 軍 金
 南 女 年
 大 東
 六
 萬 母 木 門 民
 白 父 北
 四 山 三 生 西 先 小 水 室 十
 五 王 外 月 二 人 一 日
 長 弟 中
 靑 寸 七
 土
 八
 學 韓 兄 火
"""

grades = ["1", "2", "3", "3II", "4", "4II", "5", "5II", "6", "6II", "7", "7II", "8"]

# Creating the dictionary dynamically
hanja_by_grade = {}

for grade in grades:
    # Construct the variable name (e.g., "grade1", "grade2", "grade3II", etc.)
    variable_name = f'grade{grade}'
    
    # Use globals() to access the variable value
    hanja_string = globals()[variable_name]
    
    # Remove spaces and newlines, then split into individual characters
    hanja_list = list(hanja_string.replace(" ", "").replace("\n", ""))
    
    # Add to the dictionary
    hanja_by_grade[grade] = hanja_list

# Print the dictionary to check the result
print(hanja_by_grade["7II"])

# Create a dictionary to hold the highest grade for each hanja
highest_grade_for_hanja = {}

# Iterate over grades starting from the highest to the lowest
for grade in reversed(grades):
    for hanja in hanja_by_grade[grade]:
        # If the hanja is not already in the dictionary, add it with the current grade
        if hanja not in highest_grade_for_hanja:
            highest_grade_for_hanja[hanja] = grade

# Create the final JSON structure
hanja_list = []
for hanja, grade in highest_grade_for_hanja.items():
    hanja_entry = {
        "hanja": hanja,
        "훈": None,       # Placeholder for Korean meaning
        "음": None,       # Placeholder for Korean pronunciation
        "english": None,  # Placeholder for English translation
        "grade": grade
    }
    hanja_list.append(hanja_entry)

# Convert the list to JSON format
hanja_json = json.dumps(hanja_list, ensure_ascii=False, indent=4)

# Define the file path for saving the JSON data
file_path = "hanja.json"

# Save the JSON data to the specified file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(hanja_json)

print(f"JSON data has been saved to {file_path}")

"""Grade 8: 50 Hanja characters (0,50)
Grade 7II: 50 Hanja characters ()
Grade 7: 50 Hanja characters
Grade 6II: 75 Hanja characters
Grade 6: 123 Hanja characters
Grade 5II: 100 Hanja characters
Grade 5: 100 Hanja characters
Grade 4II: 249 Hanja characters
Grade 4: 250 Hanja characters
Grade 3II: 500 Hanja characters
Grade 3: 317 Hanja characters
Grade 2: 538 Hanja characters
Grade 1: 1145 Hanja characters"""

vols = [50, 50, 50, 75, 123, 100, 100, 249, 250, 500, 317, 538, 1145]

indices = [(0, 49), (50, 99), (100, 149), (150, 224), (225, 347), (348, 447), (448, 547), (548, 796), (797, 1046), (1047, 1546), (1547, 1863), (1864, 2401), (2402, 3546)]