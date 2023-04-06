-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- # Grouping data
-- users 테이블의 전체 행 수 조회
SELECT COUNT(*) FROM users;
-- 전체 유저의 평균 balance
SELECT AVG(balance) FROM users;

-- 지역별 평균 balance 조회
-- 1) 현재 모든 유저의 지역 조회
SELECT DISTINCT country FROM users;
-- 2) 각각의 지역 별로 평균을 구해서 정리
-- 2-1) 전라북도의 평균
SELECT country, AVG(balance) FROM users WHERE country="전라북도";


-- # GROUP BY
-- 지역별 평균 balance 조회
SELECT country, AVG(balance) FROM users GROUP BY country;
-- 정렬까지
SELECT country, AVG(balance) FROM users GROUP BY country ORDER BY avg(balance) DESC;


-- 나이가 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;
-- 각 지역별로 몇 명씩 살고 있는지 조회 -> 지역별로 그룹을 나눌 필요
SELECT country COUNT(*) FROM users GROUP BY country;
-- 각 성씨가 몇 명씩 있는지 조회
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- AS 키워드를 사용해 컬럼명을 임시로 변경하여 조회 가능(*users 테이블이 변경되는 것이 아닌 조회하는 페이지만 변경)
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
-- 인원이 가장 많은 성씨 순으로 조회
SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;
-- 각 지역별 평균 나이 조회
SELECT country, AVG(age) FROM users GROUP BY country;


-- ======================================================= --
-- # Changing data
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

-- # INSERT
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
-- 이것도 가능, 하지만 컬럼 순서도 쓰는 걸 권장
INSERT INTO classmates  VALUES ('홍길동', 23, '서울');
-- 여러 행 삽입
INSERT INTO classmates 
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

-- # UPDATE
-- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정
UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid=2;


-- # DELETE
-- 5번 데이터 삭제
DELETE FROM classmates
WHERE rowid=5;
-- 삭제 확인
SELECT rowid, * FROM classmates;

-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';
-- 테이블의 모든 데이터 삭제하기 (DROP TABLE X)
DELETE FROM classmates;