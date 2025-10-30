my-board-app/
│
├── app.py                    # 메인 애플리케이션 파일
├── .gitignore               # Git 무시 파일 목록
│
├── controllers/             # 프레젠테이션 계층
│   ├── post_controller.py   # 게시글 컨트롤러
│
├── models/                  # 데이터 계층
│   ├── post.py             # 게시글 모델
│
├── services/               # 비즈니스 계층
│   ├── post_service.py     # 게시글 서비스
│
├── templates/              # HTML 템플릿
│   ├── create.html        # 게시글 생성 페이지
│   ├── detail.html        # 게시글 상세 페이지
│   └── index.html         # 메인 페이지
│
├── instance/              # Flask 인스턴스 폴더 (데이터베이스 등)
│
├── venv/                  # Python 가상 환경
│
└── README.txt             # 프로젝트 설명 파일