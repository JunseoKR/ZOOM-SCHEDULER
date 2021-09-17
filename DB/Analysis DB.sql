// ANALYSIS TABLE 생성

// [ 형식 ]
// 테이블 명 : 태장고등학교-2-9-홍준서
// 컬럼 명 : 년-월-일 | hh:mm | Process

CREATE TABLE `{}-{}-{}-{}` (`DATE` DATE NOT NULL,`TIME` TIME DEFAULT NULL,`PROCESS` char(50) DEFAULT NULL, PRIMARY KEY (`DATE`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


// ANALYSIS TABLE DATA 생성

// [ 형식 ]
// 컬럼 명 : 년-월-일 | hh:mm | Process

INSERT INTO `{}-{}-{}-{}` (DATE, TIME, PROCESS) VALUES (NOW(), NOW(), {})