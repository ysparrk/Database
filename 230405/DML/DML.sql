-- DML.sql

CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- # Simple query
-- 전체 데이터 조회
SELECT * FROM users;
-- 이름과 나이 조회
SELECT first_name, age FROM users;
-- rowid 컬럼 조회
SELECT rowid, first_name FROM users;

-- # Sorting rows
-- 이름과 나이를 나이가 어린 순서대로 조회
SELECT first_name, age FROM users ORDER BY age ASC;
SELECT first_name, age FROM users ORDER BY age;
-- 이름과 나이를 나이가 많은 순서대로 조회
SELECT first_name, age FROM users ORDER BY age DESC;
-- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;

-- # Filtering data

-- # SELECT DISTINCT
-- 모든 지역 조회하기
SELECT country FROM users;
-- 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users;
-- 지역 순으로 오름차순 정렬하여 중복 없이 모든 지역 조회
SELECT DISTINCT country FROM users ORDER BY country;
-- 이름과 지역이 중복 없이 모든 이름과 지역 조회 / 각 컬럼의 중복을 따로 계산하는 것이 아니라 두 컬럼을 하나의 집합으로 보고 중복 제거
SELECT DISTINCT first_name, country FROM users;
-- 이름과 지역 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users ORDER BY country;


-- # WHERE
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회
SELECT first_name, age, balance FROM users WHERE age >= 30;
-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;


-- # LIKE
-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';
-- 이름이 '준'으로 끝나는 사람들의 이름 조회
SELECT first_name FROM users WHERE first_name LIKE '%준';
-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';
-- 나이가 20대인 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age LIKE '2_';
-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';


-- # IN
-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회
SELECT first_name, country FROM users WHERE country IN('경기도', '강원도');
SELECT first_name, country FROM users WHERE country = '경기도' OR country = '강원도';
-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');


-- # BETWEEN
-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age BETWEEN 20 and 30;
SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;
-- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age < 20 OR age > 30;


-- # LIMIT
-- 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회
SELECT rowid, first_name FROM users LIMIT 10;
-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회
-- LIMIT 절에 지정된 행 수를 가져오기 전에 결과를 정렬하기 때문에 ORDER BY 사용 가능
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
-- 나이가 가장 어린 5명의 이름과 나이 조회
SELECT first_name, age FROM users ORDER BY age LIMIT 5;


-- # OFFSET keyword
-- 11번째부터 20번째 데이터의 rowid와 이름 조회 
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;



