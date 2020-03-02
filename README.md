# 프로그라피 6기 Django 사전과제

Django를 이용한 REST API 개발

사용 기술 스택

* Django 3.0.3
* django-rest-knox

## 기능상세

### 게시글 리스트 받아오기

```json
GET http://localhost:8000/api/posts/
```
```json
{
    "count": 101,
    "next": "http://localhost:8000/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 4,
            "title": "되는지 확인합니다",
            "description": "ㅇㅇ",
            "created_at": "2020-03-01T15:18:57.915240+09:00"
        },
        {
            "id": 5,
            "title": "post test",
            "description": "it is work?",
            "created_at": "2020-03-01T20:59:09.059510+09:00"
        },
        {
            "id": 6,
            "title": "put a",
            "description": "aa",
            "created_at": "2020-03-02T12:33:08.422534+09:00"
        },
        {
            "id": 7,
            "title": "python7",
            "description": "7's contents",
            "created_at": "2020-03-02T12:35:52.917636+09:00"
        },
        {
            "id": 8,
            "title": "python8",
            "description": "8's contents",
            "created_at": "2020-03-02T12:35:54.954146+09:00"
        }
    ]
}
```
<br>

### 게시글 상세 조회하기

```json
GET http://localhost:8000/api/posts/{id}/
```
```json
{
    "id": 5,
    "title": "post test",
    "description": "it is work?",
    "created_at": "2020-03-01T20:59:09.059510+09:00"
}
```
<br>

### 게시글 추가하기

```json
POST http://localhost:8000/api/posts/create/

HEAD
KEY : Authorization
VALUE : token "hashed 64 words"

BODY {
    "title": "heoheo",
    "description": "TEST"
}
```
```json
{
    "id": 105,
    "title": "heoheo",
    "description": "TEST",
    "created_at": "2020-03-03T08:31:47.002780+09:00"
}
```
<br>

### 가입하기

```json
POST http://localhost:8000/api/auth/register/

BODY {
    "username": "example",
    "password": "hihi"
}
```
```json
{
    "user": {
        "id": 7,
        "username": "example"
    },
    "token": "hashed 64 words"
}
```
<br>

### 로그인
```json
POST http://localhost:8000/api/auth/login/

BODY {
    "username" : "example",
    "password" : "hihi"
}
```
```json
{
    "user": {
        "id": 6,
        "username": "heoheo"
    },
    "token": "hashed 64 words"
}
```
<br>

### 로그아웃
```json
POST http://localhost:8000/api/auth/logout/

HEAD
KEY : Authorization
VALUE : token "hashed 64 words"
```
```json
default return nothing

if token is invaild

{
    "detail": "토큰이 유효하지 않습니다."
}
```
<br>

### 접속 확인

```
POST http://localhost:8000/api/auth/user/

HEAD
KEY : Authorization
VALUE : token "hashed 64 words"
```
```json
{
    "message": "인증 되었습니다."
}
```