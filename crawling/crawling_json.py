import json

data = """
{
	"lastBuildDate":"Sun, 17 Dec 2023 14:04:43 +0900",
	"total":29901,
	"start":1,
	"display":10,
	"items":[
		{
			"title":"SK하이닉스·NH농협캐피탈, 직원 채용 나서",
			"originallink":"http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20231217.99099005333",
			"link":"https://n.news.naver.com/mnews/article/658/0000060841?sid=101",
			"description":"모집 직무는 <b>Android</b> 앱 개발자, DBA, MLOps 개발자 등이다. 지원 가능 경력과 자격요건은 직무별로 다르다. 근무 지역은 서울 영등포구다. 서류 전형 합격에 대해서는 심층 면접이 이어진다. 세부 내용은 서류... ",
			"pubDate":"Sun, 17 Dec 2023 11:56:00 +0900"
		},
		{
			"title":"“졸업·새 학기, 노트북 특수 잡아라”…삼성·LG, ‘AI 노트북’ 대전 점화",
			"originallink":"https://www.ceoscoredaily.com/page/view/2023121514475212732",
			"link":"https://www.ceoscoredaily.com/page/view/2023121514475212732",
			"description":"해당 소프트웨어는 안드로이드(<b>Android</b>)나 iOS 등 OS의 제약 없이 편리하게 노트북과 스마트폰을 연결한다. 즉 그램 링크를 활용해 인터넷 연결이나 공유기 연결 없이도 삼성·애플의 스마트폰, 태블릿 등과 양방향 파일... ",
			"pubDate":"Sun, 17 Dec 2023 07:02:00 +0900"
		},
		{
			"title":"The Questions Raised by California’s Dropped Sexual Harassment Suit Aga...",
			"originallink":"https://www.nytimes.com/2023/12/16/business/dealbook/the-questions-raised-by-californias-dropped-sexual-harassment-suit-against-activision.html?partner=naver",
			"link":"https://www.nytimes.com/2023/12/16/business/dealbook/the-questions-raised-by-californias-dropped-sexual-harassment-suit-against-activision.html?partner=naver",
			"description":"The company could also be forced to open up the <b>Android</b> mobile operating system to a broader range of app stores. For instance, Epic would love to offer an app store to <b>Android</b> users. In these... ",
			"pubDate":"Sat, 16 Dec 2023 22:02:00 +0900"
		},
		{
			"title":"SK하이닉스∙콘텐츠웨이브∙현대머티리얼∙코리아세븐∙NH농협캐피탈 신입∙경...",
			"originallink":"http://www.worktoday.co.kr/news/articleView.html?idxno=46374",
			"link":"http://www.worktoday.co.kr/news/articleView.html?idxno=46374",
			"description":"모집직무는 <b>Android</b> 앱 개발자, DBA, MLOps 개발자 등이며 직무별로 채용 시 마감된다. 지원 가능 경력과 자격요건은 직무별로 상이하며 근무지역은 서울 영등포구이다. 채용절차는 △서류전형 △1차인터뷰... ",
			"pubDate":"Sat, 16 Dec 2023 10:14:00 +0900"
		},
		{
			"title":"AI 노트북 시대 열린다...삼성전자 VS LG전자 'AI 노트북' 시장서 경쟁",
			"originallink":"https://www.ajunews.com/view/20231215145321173",
			"link":"https://www.ajunews.com/view/20231215145321173",
			"description":"그램 링크는 안드로이드(<b>Android</b>)나 iOS 등 OS의 제약 없이 편리하게 노트북과 스마트폰을 연결한다. 노트북과 스마트폰의 양방향 파일 전송은 물론, 인터넷 연결이나 공유기 연결 없이도 전송이 가능하다. 그램 1대에... ",
			"pubDate":"Sat, 16 Dec 2023 09:02:00 +0900"
		},
		{
			"title":"From 'Busan Galmaegi' to 'Miracle Doosan': Cheer like a KBO pro with Eve...",
			"originallink":"https://koreajoongangdaily.joins.com/news/2023-12-16/sports/Baseball/From-Busan-Galmaegi-to-Miracle-Doosan-Cheer-like-a-KBO-pro-with-Everybodys-Baseball/1935538",
			"link":"https://sports.news.naver.com/news.nhn?oid=640&aid=0000047370",
			"description":"It’s totally free, available to both iPhone and <b>Android</b> users, all the more important for an... their <b>Android</b> version. But what sets this app apart, according to the team, is the thought behind... ",
			"pubDate":"Sat, 16 Dec 2023 08:31:00 +0900"
		},
		{
			"title":"&quot;누가 더 똑똑할까&quot;…갤럭시 북 VS LG 그램, AI 노트북 대전",
			"originallink":"https://www.etoday.co.kr/news/view/2312361",
			"link":"https://www.etoday.co.kr/news/view/2312361",
			"description":"그램 링크는 안드로이드(<b>Android</b>)나 iOS 등 OS의 제약 없이 편리하게 노트북과 스마트폰을 연결한다. 노트북과 스마트폰의 양방향 파일 전송은 물론, 인터넷 연결이나 공유기 연결 없이도 전송할 수 있다. 그램... ",
			"pubDate":"Sat, 16 Dec 2023 07:02:00 +0900"
		},
		{
			"title":"Call translation services new battleground in AI race",
			"originallink":"https://koreajoongangdaily.joins.com/news/2023-12-16/national/kcampus/Call-translation-services-new-battleground-in-AI-race/1936812",
			"link":"https://n.news.naver.com/mnews/article/640/0000047368?sid=102",
			"description":"“Currently, only iPhone users can use the translation service, but <b>Android</b> users will soon be able to use it as well,” SK Telecom said. The rollout of the new service is part of a move by SK... ",
			"pubDate":"Sat, 16 Dec 2023 06:00:00 +0900"
		},
		{
			"title":"AI 노트북 ‘LG 그램’ 출시…삼성과 시장 선도 경쟁 시작",
			"originallink":"https://www.khan.co.kr/economy/market-trend/article/202312152108025",
			"link":"https://n.news.naver.com/mnews/article/032/0003267745?sid=101",
			"description":"그램 링크는 구글 안드로이드(<b>Android</b>)나 애플 iOS 등 OS 제약 없이 편리하게 노트북과 스마트폰을 최대 10대까지 연결해 준다. 노트북과 스마트폰의 양방향 파일 전송은 물론, 인터넷 연결이나 공유기 없이도 파일... ",
			"pubDate":"Fri, 15 Dec 2023 21:09:00 +0900"
		},
		{
			"title":"LG전자, 최신 AI CPU 탑재한 '24년형 LG 그램' 판매",
			"originallink":"https://www.gpkorea.com/news/articleView.html?idxno=108377",
			"link":"https://www.gpkorea.com/news/articleView.html?idxno=108377",
			"description":"LG 그램 최초로 안드로이드(<b>Android</b>)나 iOS 등 OS 연결 제약이 없고, 인터넷에 연결하지 않아도 파일 전송이 가능한 소프트웨어 '그램 링크(gram Link)'가 탑재된다. LG전자는 신제품의 가격을 이전 세대와... ",
			"pubDate":"Fri, 15 Dec 2023 17:48:00 +0900"
		}
	]
}
"""

json_data = json.loads(data)
print(json_data["items"][0]['title'])
print(json_data["items"][0]['link'])
