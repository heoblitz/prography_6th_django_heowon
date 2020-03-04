# 프로그라피 6기 Django 사전과제

Django를 이용한 REST API 개발

## 사용 기술 스택

* Django 3.0.3
* Django REST framework
* Django-rest-knox
* AWS EC2

## API 액세스 권한

* 게시글 조회는 모두 접근 가능합니다.

* 추가 & 수정 & 삭제 API 은 token 을 통해 요청해야 합니다.

* 사용자 별로 인증 권한이 부여되며, 다른 유저 게시글은 삭제 및 수정이 불가합니다.

* 회원가입(로그인) -> 게시글 추가, 수정, 삭제 -> 로그아웃

* TEST 계정

    * username : steve
    * password : 1234

### 

## 기능상세

### 게시글 리스트 받아오기

```json
GET http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/posts/
```
```json
{
    "count": 101,
    "next": "http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 210,
            "author": "heoblitz",
            "title": "my first posts!",
            "description": "amazing",
            "created_at": "2020-03-03T16:06:28.447788+09:00"
        },
        {
            "id": 209,
            "author": "steve",
            "title": "100's title",
            "description": "100's contents",
            "created_at": "2020-03-03T16:00:01.324205+09:00"
        },
        {
            "id": 208,
            "author": "steve",
            "title": "99's title",
            "description": "99's contents",
            "created_at": "2020-03-03T15:59:59.287534+09:00"
        },
        {
            "id": 207,
            "author": "steve",
            "title": "98's title",
            "description": "98's contents",
            "created_at": "2020-03-03T15:59:57.264696+09:00"
        },
        {
            "id": 206,
            "author": "steve",
            "title": "97's title",
            "description": "97's contents",
            "created_at": "2020-03-03T15:59:55.237856+09:00"
        }
    ]
}
```
<br>

### 게시글 상세 조회하기

```json
GET http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/posts/{id}/
```
```json
{
    "id": 130,
    "author": "steve",
    "title": "21's title",
    "description": "21's contents",
    "created_at": "2020-03-03T15:57:21.148809+09:00"
}
```
<br>

### 게시글 추가하기

```json
POST http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/posts/create/

HEAD
KEY : Authorization
VALUE : token "hashed 64 words"

BODY {
    "title": "hello guys",
    "description": "it is TEST"
}
```
```json
{
    "id": 110,
    "author": "new_person",
    "title": "hello guys",
    "description": "it is TEST",
    "created_at": "2020-03-03T13:49:18.030282+09:00"
}
```
<br>

### 회원가입

```json
POST http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/auth/register/

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
POST http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/auth/login/

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
POST http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/auth/logout/

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
POST http://ec2-13-125-237-249.ap-northeast-2.compute.amazonaws.com/api/auth/user/

HEAD
KEY : Authorization
VALUE : token "hashed 64 words"
```
```json
{
    "message": "인증 되었습니다."
}
```