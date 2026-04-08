# request는 
# redirect는 사용자를 다른 페이지로 보내버리기
from Flask import Flask, request, redirect

app = Flask(__name__)

# 임시 데이터베이스 (서버 메모리에 저장)
next_id = 4

# 여기서 id 는 구분을 위함임
topics = [
    {'id': 1, 'title': '사과', 'body': '빨갛고 새콤달콤한 과일'},
    {'id': 2, 'title': '초콜릿', 'body': '달콤한 간식'},
    {'id': 3, 'title': '빵', 'body': '부드러운 음식'}
]

# --- READ (조회) ---

# 메인 페이지 조회
@app.route('/')
def index():
    # topics 리스트를 순서대로 돌면서 <li> 태그를 하나씩 이어 붙임
    li_tags = ""
    for topic in topics:
        li_tags += f'''
        <li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>
        '''
    return f'''
<h1>WEB Storage</h1>
    <ol>{li_tags}</ol>
    
    <a href="/create">+ 글쓰기</a>
    '''




# 2. 상세 페이지: 특정 글 읽기
@app.route('/read/<int:id>/')
def read(id):
    # id가 일치하는 글을 찾아서 반환
    for topic in topics:
        if topic['id'] == id:
            return f'<h1>{topic["title"]}</h1>{topic["body"]}<br><br><a href="/">목록으로</a>'

    # 끝까지 못 찾으면 404 에러
    return '글이 없습니다.', 404





# --- CREATE (생성) ---

# 3. 글쓰기 페이지
@app.route('/create/', methods=['GET', 'POST'])
def create():
    # GET 요청: 글쓰기 폼을 화면에 보여줌
    if request.method == 'GET':
        return '''
            <form action="/create/" method="POST">
                <input type="text" name="title" placeholder="제목"><br>
                <textarea name="body" placeholder="내용"></textarea><br>
                <input type="submit" value="저장">
            </form>
        '''

    # POST 요청: 폼에서 보낸 데이터를 저장
    elif request.method == 'POST':
        global next_id

        # 폼 데이터로 새 글 딕셔너리 만들기
        new_topic = {
            'id': next_id,
            'title': request.form['title'],
            'body': request.form['body']
        }

        # 리스트에 추가
        topics.append(new_topic)

        # 저장한 글 페이지로 이동
        next_id += 1
        return redirect(f'/read/{next_id - 1}/')



if __name__ == '__main__':
    app.run(port=5001, debug=True)
