CREATE TABLE IF NOT EXISTS Movie(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    caption VARCHAR(500) NOT NULL,
    teather VARCHAR(50) NOT NULL,
    price INT(6) NOT NULL,
    img VARCHAR(500) NOT NULL
);

INSERT INTO Movie(title, caption, teather, price, img) VALUES
('【Midjourney】AIでイラストを描こう！ -人工知能によるテキストからの画像生成-', 'Midjourneyを使い、AI（人工知能）による文章からの画像生成について学びましょう。AIによる画像生成に興味のある方、趣味として楽しみたい方、素材を自動生成したい方、新たなアートの形を模索したい方におすすめです。', '我妻 幸長', 1800, 'https://img-c.udemycdn.com/course/240x135/4838962_1201.jpg'),
('本当にわかる、AI時代の数学【超初心者からの数学入門】', '数学アレルギーでも大丈夫／やさしく丁寧な解説／コード無し　キーワード:基礎／数学／行列／線形代数／ベクトル／微分／データサイエンス／AI／機械学習／ディープラーニング／データドリブン／人工知能／GPT', '憲児 近藤', 1800, 'https://img-c.udemycdn.com/course/240x135/3818086_840c.jpg'),
('【初心者向けの投資法！インデックス投資を学び、投資家になろう！初学者向け】データ分析コンペで楽しみながら学べるPython×データ分析講座', '世界一有名な投資家ウォーレンバフェットも認めるインデックス投資を学びましょう', '井上 ヨウスケ', 1900, 'https://img-c.udemycdn.com/course/240x135/1663518_c06e.jpg'),
('MBA英語で金融と会計の基本を学ぶ｜初心者向けの実用英語', '【ネイティブのゆっくり英語】頑張る必要は一切ありません！まずは簡単な会計専門用語から少しずつ挑戦していきましょう。この講座は力を抜いてゆっくり金融系英語を身に着けていきたい初心者を考えて作りました。', 'Vivian (ビビアン) He', 1800,'https://img-c.udemycdn.com/course/240x135/4545382_a791.jpg'),
('銀行取引に自信が持てるようになる融資マニュアル', 'あなたはもっと有利な条件で融資が受けたいと思いませんか？銀行や融資についての正しい知識をつけて銀行と良好な関係を築き、金利交渉や担保交渉に自信をもって臨めるようになりましょう！', '川原 拓馬', 2000, 'https://img-c.udemycdn.com/course/240x135/4663174_5d7c_4.jpg'),
('【金融知識/ビジネススキル】経済指標の見方・活用方法を運用会社社員＆エコノミストがビジネスパーソンの皆様へ教えます', '金融知識をビジネスパーソンの必要スキルに～経済指標編～', '三菱UFJ国際投信 株式会社', 1800, 'https://img-c.udemycdn.com/course/240x135/5098790_9028_4.jpg'),
('【会社法を学ぼう！】いちばんわかりやすい「会社の仕組み」', '《会社員なら知らなきゃヤバい！》会社は誰もの？、会社の種類と特徴、「所有と経営の分離」とは？、株主の権力、取締役や監査役の権限、間接金融と直接金融の違い', '公認会計士 川口宏之', 27800, 'https://img-c.udemycdn.com/course/240x135/4890736_0abe.jpg'),
('【外国為替/ビジネススキル】外国為替の簡単な考え方・伝え方を運用会社がビジネスパーソンの皆様へ教えます', '金融知識をビジネスパーソンの必要スキルに～外国為替編～', '三菱UFJ国際投信 株式会社', 2400, 'https://img-c.udemycdn.com/course/240x135/4884976_c70d.jpg'),
('【債券知識/ビジネススキル】債券知識・活用方法を運用会社社員がビジネスパーソンの皆様へ教えます', '知識をビジネスパーソンの必要スキルに～債券編～', '三菱UFJ国際投信 株式会社', 2400, 'https://img-c.udemycdn.com/course/240x135/4884976_c70d.jpg'),
('【税金・年金・保険】の仕組みを知らないと搾取される説', 'プルデンシャルの営業マンに搾取されたく無い方はぜひご覧ください。お金に困っていない人は大丈夫です。', '叶 平川', 9800, 'https://img-b.udemycdn.com/course/240x135/1325556_6a74_2.jpg'),
('投資を始めたい人必見！支出を減らし、投資ができるようになる資産形成マニュアル', '投資を始める前にその元手を作るために家計を見直ししませんか？見直し方法から投資の方法まで全て教えます', '井上 ヨウスケ, 石崎力也', 19800, 'https://img-c.udemycdn.com/course/240x135/1595452_97fe_2.jpg'),
('iDeCo入門　FPが教える！基礎からわかる個人型確定拠出年金（イデコ）の始め方', '節税しながら無理ない積み立て投資　人生100年時代でも老後は安心 掛金は全額所得控除、運用収益はすべて非課税', '文丘 雄清', 27800, 'https://img-c.udemycdn.com/course/240x135/4609642_bfd8_2.jpg'),
('【株式知識/ビジネススキル】株式知識・活用方法を運用会社社員がビジネスパーソンの皆様へ教えます', '知識をビジネスパーソンの必要スキルに～株式編～', '三菱UFJ国際投信 株式会社', 2400, 'https://img-c.udemycdn.com/course/240x135/5235556_6fc1.jpg');