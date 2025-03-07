--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Ubuntu 16.4-0ubuntu0.24.04.2)
-- Dumped by pg_dump version 16.4 (Ubuntu 16.4-0ubuntu0.24.04.2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.auth_group (id, name) FROM stdin;
1	super_admin
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	sales	salesuser
8	customers	customer
9	token_blacklist	blacklistedtoken
10	token_blacklist	outstandingtoken
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add 销售用户	7	add_salesuser
26	Can change 销售用户	7	change_salesuser
27	Can delete 销售用户	7	delete_salesuser
28	Can view 销售用户	7	view_salesuser
29	Can add 客户	8	add_customer
30	Can change 客户	8	change_customer
31	Can delete 客户	8	delete_customer
32	Can view 客户	8	view_customer
33	Can add blacklisted token	9	add_blacklistedtoken
34	Can change blacklisted token	9	change_blacklistedtoken
35	Can delete blacklisted token	9	delete_blacklistedtoken
36	Can view blacklisted token	9	view_blacklistedtoken
37	Can add outstanding token	10	add_outstandingtoken
38	Can change outstanding token	10	change_outstandingtoken
39	Can delete outstanding token	10	delete_outstandingtoken
40	Can view outstanding token	10	view_outstandingtoken
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$870000$YpxxQgZB8PDCLKxrcBUabH$g6Oj3hmz8svEjlnARwy3MHPdplAmM4S40qYA5d3K6Q0=	2024-10-06 16:57:25.349523+08	t	austin				t	t	2024-10-06 16:24:55.363537+08
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: sales_salesuser; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.sales_salesuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role, group_leader_id) FROM stdin;
36	pbkdf2_sha256$870000$OouzWk0AVoCtW7khzv156b$GGq9vg4ShN3s4CnR/xlW5zsSu6aJ8HSFG4KYmOw5KK8=	\N	f	刘永林	永林	刘		f	t	2024-10-21 11:40:00+08	user	8
37	pbkdf2_sha256$870000$pIY9mbrzCHyNYyVOf9fjdI$TKGP9DSxcAe+DI9qaEQXcg29sixG8a5uQnfSuPy1Hn4=	\N	f	张海玲	海玲	张		f	t	2024-10-21 11:40:00+08	user	8
8	pbkdf2_sha256$870000$pqOlyY1OvwVFQZ5ShETz52$39kbIGql88SXN2UGNXqxTCGqzN7ZtUD2hDww+xnEow0=	2024-10-08 15:20:00+08	t	董婷婷				t	t	2024-10-08 15:19:00+08	admin	\N
13	pbkdf2_sha256$870000$jhwgqdD1yrienoIR5QoVwO$dL62ioA0rE0oN88cEw5l7DeekmivKioBZLUEMBux7Ts=	\N	f	胡夏阳	夏阳	胡		f	t	2024-10-08 17:44:00+08	user	4
18	pbkdf2_sha256$870000$yI5DxqiL7dLA4rtX4CXgS7$03N6wfXqpWZZfIN/2o4jOKsfwzw8beD9jZg6WBiYWUg=	\N	f	魏豪	豪	魏		f	t	2024-10-08 17:58:00+08	user	8
17	pbkdf2_sha256$870000$JjY2sodYChYgQGMA4PNrR5$uE3Hhv/kNLV80IYE4KWeEITSLcM1MsxP5mbEAUN3HmE=	\N	f	张俊				f	t	2024-10-08 17:56:00+08	user	13
19	pbkdf2_sha256$870000$1wsenE5w4D7e6hn2G83wV6$p5O1o5KjQhPF2B/i7PuNIkNySAqV/3F+U5Wa3NMw+NE=	\N	f	吴小维				f	t	2024-10-08 17:58:00+08	user	13
29	pbkdf2_sha256$870000$eOljSCGkeG8yePZBigmTik$nFP1KmjWzkbUvA9EtoVWW/SpdkU80E7gYKPIGTRrB+k=	2024-10-08 18:09:00+08	t	陈予琳				t	t	2024-10-08 18:08:00+08	admin	\N
11	pbkdf2_sha256$870000$cswbCthoCO3nIbvjKz7z5Y$/1s2/ZPzkS1LOyCOepQ6idbpTxdQiHArXtqyqF5BMQ8=	\N	f	晴妹				f	t	2024-10-08 15:44:00+08	user	4
20	pbkdf2_sha256$870000$3Sb0Xv9dp3u9Ybr461qTth$WzTGRVL/P97I2w2ZUBGUJn1x+kf/zL7o4kvC1sHl05U=	\N	f	邓小亮	小亮	邓		f	t	2024-10-08 17:59:00+08	user	4
24	pbkdf2_sha256$870000$q91psXQvlsE72c66Ms0E5q$McRxmZWEC2n7Z1QNsu0uKSpuTxh8652vXKQkmPsiGBs=	\N	f	张凯钦	凯钦	张		f	t	2024-10-08 18:04:00+08	user	4
33	pbkdf2_sha256$870000$oyr3GePvIyLdsLrxY08V92$WYpucafivYcMj5wxLyDL2mvKMUocd/dnW3A4x8qSQx4=	\N	f	丁丽婷	丽婷	丁		f	t	2024-10-21 09:20:00+08	user	8
34	pbkdf2_sha256$870000$PjRQSrT6iALwtbLT6Qw04H$6uSwKARsnVh7OKqTGEq9Ut5kwwF8U2UV1cFut8TlR5c=	\N	f	陈怡君	怡君	陈		f	t	2024-10-21 09:21:00+08	user	8
28	pbkdf2_sha256$870000$39MPOANk52gOQcL8sv4hSF$QyEG/kzSA3+u4YxTiKOHy2SSWQU0wrdYD+pxT+oKWVA=	\N	f	朱龙冲	龙冲	朱		f	t	2024-10-08 18:07:00+08	user	4
32	pbkdf2_sha256$870000$410roo58N8xi97vQX29bxJ$rnv1lSfza/48gUK/RXUloNgGB3oLCLgxINiajg3oiWU=	\N	t	任侠				t	t	2024-10-18 19:17:00+08	admin	\N
31	pbkdf2_sha256$870000$7oufIssUaFv3oRKlMxiZUk$kaYcBJbwBrrei/o8+4ZMoB8Ai+SH7BU4Wz/kvD9DDeY=	\N	f	丁雨波				f	t	2024-10-08 18:40:00+08	user	4
14	pbkdf2_sha256$870000$FWQWJH0umYi71VPkIyItfL$5EzvbSPScqkbQRJobPKp96WkDl38C0Mrkr8fObeykb4=	\N	f	秦嘉豪	嘉豪	秦		f	t	2024-10-08 17:47:00+08	user	4
26	pbkdf2_sha256$870000$eiceeQNu3zUmBKfiZs6wu5$uJpFtzJkBCQQvVIUmOiOV7lw2DD5O86Z2EdfFarmnSM=	\N	f	胡小婷	小婷	胡		f	t	2024-10-08 18:05:00+08	user	4
27	pbkdf2_sha256$870000$qSFZBT8gBySVRIiA6PU9bf$sA3ZcQMtRk/AnkdIEoJoe8lL5s9XaPdgAleSDXpaR14=	\N	f	邹敏	敏	邹		f	t	2024-10-08 18:06:00+08	user	4
35	pbkdf2_sha256$870000$7uLnE55o2KLt8mWBYBFkUJ$aqdfVGr/jdIrHExqace4xKlRcMBXH79ANTqag8BKACo=	\N	f	金坤香	坤香	金		f	t	2024-10-21 09:46:00+08	user	8
22	pbkdf2_sha256$870000$XfBwj7Za5O5Dnab3dR75LG$IgN1fwwBpkvFAG4pMdgmuRaCD+QAOocJo5tGW+62Jek=	\N	f	李小伟	小伟	李		f	t	2024-10-08 18:01:00+08	user	4
6	pbkdf2_sha256$870000$DFSLyNbhLWrZox5qX4ovzQ$mRZcxUHtti06zyZTKfFCVdtRyeZrPVrumOkue1jp0Qk=	\N	f	李美钰	美钰	李		f	t	2024-10-08 14:29:00+08	user	4
25	pbkdf2_sha256$870000$riD6v1RwaunQV9MLTpXmIC$rFrlQxmkWHKk6VCOXGDp881bN7fQnwQ5draVie3cF80=	\N	f	王微伟	微伟	王		f	t	2024-10-08 18:05:00+08	user	4
1	pbkdf2_sha256$600000$UQc85lxlcFKZqgPtQY1fna$3D6roZSy3c7kz4godiO5O/v17R3wjPX1DduvV+SETyg=	2024-11-13 15:25:55.048925+08	t	austin				t	t	2024-10-06 18:40:00+08	admin	\N
2	pbkdf2_sha256$870000$PVTeNm0I5BUPwRJo4ZP5ii$PJFz5l5LywzEeYTgSr5lCR/qfuHtQwGz44dzCUVAg9c=	2024-11-10 23:19:48.271493+08	f	冷子慧	子慧	冷		f	t	2024-10-08 10:10:00+08	user	4
4	pbkdf2_sha256$870000$KKJCCREAqnwAahYOmmjuxS$0tYIQkAQuFL9YdCWRlHMNXmDo3R27fALkMmcvBdUwvA=	2024-11-10 23:27:03.482475+08	f	汪城波				f	t	2024-10-08 14:17:00+08	group_leader	4
\.


--
-- Data for Name: customers_customer; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.customers_customer (id, name, phone, education, major_category, status, address, city, intention, is_closed, is_invited, is_joined, data_source, attended_first_live, attended_second_live, first_day_watch_duration, second_day_watch_duration, created_at, updated_at, description, created_by_id, updated_by_id, is_contacted, is_wechat_added, additional_students, comments_count, deal_14_days_checked, deal_14_days_text, deal_21_days_checked, deal_21_days_text, deal_7_days_checked, deal_7_days_text, first_day_feedback, is_course_reminder, persona_chat, second_day_feedback, wechat_name, cloud_computing_promotion_content, customer_needs_analysis, customer_personality_analysis, student_batch, supervisor_comments) FROM stdin;
8	未知	15290909280	未知	未知	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 14:45:00.934593+08	2024-10-08 14:45:00.934609+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
9	未知	13672209676	未知	非IT	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:01:42.919714+08	2024-10-08 15:01:42.919728+08	通话中	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
10	未知	13667753540	未知	未知	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:02:54.147675+08	2024-10-08 15:02:54.147689+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
41	汪皓	18162935490	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 17:29:00.063051+08	2024-10-08 17:29:00.063082+08	加微信待通过	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
12	未知	18883939218	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:05:12.34693+08	2024-10-08 15:05:12.346945+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
13	未知	17521275135	本科	IT	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:08:36.35023+08	2024-10-08 15:08:36.350244+08	来了解云计算这个行业	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
14	未知	15352392897	大专	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:09:24.054894+08	2024-10-08 15:09:24.054922+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
15	官子健	15361001882	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:13:11.708931+08	2024-10-08 15:13:11.708947+08	现在有事在忙，急忙挂断电话	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
16	未知	18002552881	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:14:26.789701+08	2024-10-08 15:14:26.789715+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
17	未知	13126406544	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:15:03.22643+08	2024-10-08 15:15:03.226444+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
18	刘石宝	17687922457	本科	IT	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:18:43.682297+08	2024-10-08 15:18:43.682312+08	来了解云计算	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
19	未知	17260666250	未知	未知	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:21:45.051204+08	2024-10-08 15:21:45.051218+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
20	未知	15664912573	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:22:30.365685+08	2024-10-08 15:22:30.3657+08	未接	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
21	刘恩祥	18286624490	本科	IT	在职	未知	未知	中	f	f	f	AI数据	f	f	0	0	2024-10-08 15:24:18.944462+08	2024-10-08 15:24:18.944477+08	做芯片研发，月薪22-27k	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
22	未知	13346301517	本科	IT	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 15:25:18.40736+08	2024-10-08 15:25:18.407374+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
24	未知	19507416900	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:23:16.625763+08	2024-10-08 16:23:16.625777+08	未接	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
28	未知	15171939188	本科	IT	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:27:34.10493+08	2024-10-08 16:27:34.104946+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
29	张智勇	17537615894	本科	IT	待业	未知	未知	中	f	f	f	AI数据	f	f	0	0	2024-10-08 16:29:19.12121+08	2024-10-08 16:29:19.121226+08	25届毕业生，想往Java方向走，不太想换方向	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
30	周志远	13600390509	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:29:48.916874+08	2024-10-08 16:29:48.916888+08	应届待业	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
31	瑶正阳	18732229965	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:31:14.7523+08	2024-10-08 16:31:14.752314+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
32	张世龙	18691910601	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:32:07.516728+08	2024-10-08 16:32:07.516743+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
33	曾汝兰	13510453171	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:32:51.28253+08	2024-10-08 16:32:51.282548+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
34	李拜天	15138237214	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:33:54.287232+08	2024-10-08 16:33:54.287248+08	未接盲加	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
37	毛一婷	19857598991	未知	未知	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 16:39:44.229332+08	2024-10-08 16:39:44.229347+08	未接	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
39	王嘉文	17829157703	大专	IT	在职	不限	陕西	中	f	f	f	AI数据	f	f	0	0	2024-10-08 16:43:38.688215+08	2024-10-08 16:43:38.688228+08	软件技术，之前薪资5k，想往上发展，之后打算从事运维方向	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
42	潘绵科	15018000591	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 17:30:01.603274+08	2024-10-08 17:30:01.603288+08	未接	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
43	王智宇	15637797334	研究生及以上	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 17:33:17.814207+08	2024-10-08 17:33:17.814221+08	研究生在快递公司做管理层	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
44	王柯	17521554173	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 17:53:28.373536+08	2024-10-08 17:53:28.37355+08	了解云计算	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
45	蒋双双	18528017939	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:02:52.224731+08	2024-10-08 18:02:52.224746+08	1	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
46	王胜	19828753879	本科	非IT	待业	成都	广汉	中	f	t	t	AI数据	f	f	0	0	2024-10-08 18:05:46.174386+08	2024-10-08 18:05:46.174401+08	偏向于维护交换机路由器之类的工作，还有一个月上完课，	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
47	章子杨	13860060153	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:14:02.805627+08	2024-10-08 18:14:02.805642+08	未接	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
35	朱方帅	13593948824	研究生及以上	IT	待业	未知	未知	中	f	t	t	AI数据	f	f	0	0	2024-10-08 16:36:25.532711+08	2024-10-08 18:06:25.247724+08	25届毕业生，期望薪资1.8w	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
36	杜开金	13419084895	本科	IT	在职	成都	成都	高	f	t	t	AI数据	f	f	0	0	2024-10-08 16:38:44.446472+08	2024-10-08 18:06:39.229974+08	之前做机房运维，期望薪资5-6，了解过阿里云华为云证书，有想往这个行业发展，	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
7	未知	17864426872	本科	非IT	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 14:22:59.788693+08	2024-11-02 09:54:19.051237+08	毕业两年，建筑工程技术专业，想往工程管理方面发展	2	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	0	大傻逼
38	汪高尚	18629501075	本科	IT	在职	未知	未知	高	f	t	t	AI数据	f	f	0	0	2024-10-08 16:41:54.870293+08	2024-10-08 18:07:05.516953+08	了解价格在听宣讲，接受费用	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
48	未知	19925723494	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:14:52.003419+08	2024-10-08 18:14:52.003434+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
49	蔡万	18705577647	本科	非IT	在职	杭州	江苏	中	f	t	t	AI数据	f	f	0	0	2024-10-08 18:16:33.829131+08	2024-10-08 18:16:33.829147+08	从事海工类工作，毕业一年，想换行业和城市发展	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
50	贾川琨	16634221314	本科	未知	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:17:52.421115+08	2024-10-08 18:17:52.421131+08	微信未回复	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
25	刘堂濠	15013146024	本科	IT	在职	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 16:25:34.996838+08	2024-10-08 18:22:09.071274+08	应届待业	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
27	叶真熙	18677411884	本科	IT	在职	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 16:27:19.753643+08	2024-10-08 18:22:35.350855+08	大学毕业两年，有工作经历，看看云计算行情	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
40	杨鹏	15779718699	大专	IT	在职	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 17:26:09.033523+08	2024-10-08 18:22:49.6121+08	人工智能，了解云计算	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
51	谭鹏飞	18603323010	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:20:39.174175+08	2024-10-08 18:20:39.174192+08	不想了解	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
52	徐	15268332426	本科	IT	待业	杭州	杭州	中	f	t	t	AI数据	f	f	0	0	2024-10-08 18:23:03.861938+08	2024-10-08 18:23:03.861956+08	24届，物联网，本科，杭州，待业	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
53	吴新林	18059558043	大专	非IT	待业	全国都可以	南平	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:25:23.363049+08	2024-10-08 18:25:23.363086+08	21岁，25届，电子信息，在上课，南平，全国可取	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
54	未知	15121733697	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:26:01.939818+08	2024-10-08 18:26:01.939834+08		27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
55	毛鸿麟	13026522269	未知	未知	待业	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:26:14.994833+08	2024-10-08 18:26:14.994848+08		26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
56	王若洋	19834040882	本科	非IT	待业	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:27:07.358189+08	2024-10-08 18:27:07.358204+08	24岁，经济类	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
57	肖均	18990930691	未知	未知	待业	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:28:14.702289+08	2024-10-08 18:28:14.702304+08		26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
59	梁赵玮	18718368641	本科	非IT	在职	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:29:00.522757+08	2024-10-08 18:29:00.522774+08	土木专业	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
60	未知	13670506422	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:29:11.284427+08	2024-10-08 18:29:11.284441+08		27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
61	刘珊	15868496184	未知	未知	未知	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:29:35.964287+08	2024-10-08 18:29:35.964302+08		26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
63	祈祷	13106946164	未知	未知	待业	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:30:26.623591+08	2024-10-08 18:30:26.623606+08		26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
64	未知	15623886268	未知	未知	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:30:39.718257+08	2024-10-08 18:30:39.718271+08		27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
65	KW	18926356050	未知	未知	未知	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 18:30:53.680371+08	2024-10-08 18:30:53.680387+08		26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
62	未知	16670050562	本科	IT	待业	未知	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-08 18:30:10.119391+08	2024-10-08 18:31:08.55463+08		27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
58	李	18580470622	本科	非IT	待业	未知	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-08 18:28:22.817726+08	2024-10-08 18:31:49.116516+08	25届数量经济学	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
66	未知	18004582470	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:32:18.711265+08	2024-10-08 18:32:18.71128+08		27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
67	未知	18857375167	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:32:41.921312+08	2024-10-08 18:32:41.921327+08		27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
68	未知	15194684106	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:38:18.708448+08	2024-10-08 18:38:18.708469+08		24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
69	未知	13537511584	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:40:33.984661+08	2024-10-08 18:40:33.984677+08	不方便	24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
70	未知	19147950631	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:41:11.850632+08	2024-10-08 18:41:11.850647+08	不需要找到工作了	24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
71	未知	18307747972	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:41:44.697661+08	2024-10-08 18:41:44.697676+08	不参加	24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
72	未知	18307747972	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:42:37.888368+08	2024-10-08 18:42:37.888384+08	不适合	24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
73	未知	17388977159	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:44:11.707101+08	2024-10-08 18:44:11.707116+08		24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
74	未知	13726998893	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:44:43.098703+08	2024-10-08 18:44:43.098718+08	待通过	24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
75	未知	15607008802	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:45:41.766822+08	2024-10-08 18:45:41.766836+08		24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
76	未知	13264866712	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:46:00.422705+08	2024-10-08 18:46:00.42272+08		24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
77	未知	15575954832	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:46:20.031744+08	2024-10-08 18:46:20.031759+08		24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
78	未知	17778970953	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-08 18:46:37.793444+08	2024-10-08 18:46:37.793478+08		24	24	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
79	凯特	15619865163	本科	IT	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-09 10:08:46.378199+08	2024-10-09 10:08:46.378213+08	不感兴趣，挂断	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
80	张佳乐	15592040317	未知	未知	未知	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-09 10:15:52.658117+08	2024-10-09 10:15:52.658133+08	未接通	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
81	李海韬	17355156241	本科	IT	待业	未知	未知	中	f	f	f	AI数据	f	f	0	0	2024-10-09 10:53:02.009463+08	2024-10-09 11:10:27.28224+08	25届感兴趣	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
82	白学涛	15693522219	大专	非IT	待业	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-09 11:11:31.325744+08	2024-10-09 11:11:31.325759+08		22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
83	陈智鹏	18320326435	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-09 11:17:27.461801+08	2024-10-09 11:17:27.461823+08	不感兴趣	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
84	鲍建伟	15057104700	本科	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-09 11:28:18.053523+08	2024-10-09 11:28:18.053538+08	不感兴趣	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
86	徐颖	13570645993	未知	IT	在职	未知	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-09 11:50:59.468776+08	2024-10-09 11:50:59.468813+08	不感兴趣	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
85	彭旭	19526174614	本科	IT	在职	未知	未知	中	f	t	f	AI数据	f	f	0	0	2024-10-09 11:42:37.030424+08	2024-10-09 14:16:06.733068+08	感兴趣	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
87	候岚清	18163662129	本科	非IT	待业	未知	未知	中	f	t	t	AI数据	f	f	0	0	2024-10-09 15:15:43.175296+08	2024-10-09 15:15:43.175314+08	23届电气刚离职	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
88	黄胤忠	18126842306	本科	IT	待业	未知	未知	中	f	f	f	AI数据	f	f	0	0	2024-10-09 15:33:39.63168+08	2024-10-09 15:33:39.631695+08	去年毕业，感兴趣	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
26	周龙	15023848016	本科	IT	待业	重庆	重庆	高	f	t	t	AI数据	f	f	0	0	2024-10-08 16:26:57.847274+08	2024-10-13 13:46:50.77316+08	在安恒实习过做测试，对互联网企业很感兴趣，期望薪资8-10\n所以你对他的判断是什么？	2	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
23	代金胜	15978582750	本科	IT	在职	未知	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-08 16:22:24.08842+08	2024-10-13 17:48:47.259961+08	计算机应届待业\n持续跟进	6	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
91	测试客户334	15198713517	本科	IT	在职	未知	缅甸	高	f	f	t	AI数据	f	t	0	0	2024-10-14 18:04:44.889074+08	2024-10-14 18:05:37.221019+08	傻逼	1	1	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
93	未知	15198713510	本科	IT	在职	北京	南昌	低	t	t	f	AI数据	f	t	0	0	2024-10-14 18:14:37.273309+08	2024-10-14 18:14:37.273323+08		1	1	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
95	测试客户00	15198713512	本科	IT	在职	重庆	南昌	低	t	t	t	AI数据	t	f	0	0	2024-10-14 18:24:03.54549+08	2024-10-14 18:24:03.545505+08	帅哥	1	1	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
94	测试客户112	44433333333	本科	IT	在职	南昌	南昌	低	f	f	f	AI数据	t	f	0	0	2024-10-14 18:16:16.326835+08	2024-10-17 00:43:50.143841+08		1	1	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	不考虑	\N	[]	[]	[]	0	\N
117	张志强	17703435463	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:12:00.430032+08	2024-10-21 10:12:00.430063+08	在忙，加微信聊	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
119	未知	18667146325	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:19:11.626325+08	2024-10-21 10:19:11.62634+08	不感兴趣没有转行打算	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
138	邬荣人	18845104259	研究生及以上	IT	待业	\N	哈尔滨	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:02:05.255154+08	2024-10-21 11:02:05.255169+08	硕士，信息与通信专业，在哈尔滨，想回南方发展，25年毕业	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Wr²	[]	[]	["理性"]	32	\N
115	张雪松	18223401125	未知	未知	待业	\N	重庆	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:10:39.841486+08	2024-10-21 10:24:00.996079+08	挂断	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	࿐Cedar꧔ꦿ࿐	[]	[]	[]	32	\N
121	万俊杰	17851416527	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:24:39.450372+08	2024-10-21 10:24:39.450389+08	未知	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	青年	[]	[]	[]	32	\N
126	卫将豪	13835908096	研究生及以上	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:38:07.850692+08	2024-10-21 10:38:07.850709+08	研究生学历，目前研三，武汉、深圳都可以，期望薪资12k，后端开发方向的	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	["云计算的薪资和发展空间"]	["是否表示工作难找", "是否了解过云计算"]	[]	32	\N
130	未知	18100864706	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:48:38.943299+08	2024-10-21 10:48:38.943313+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
128	王刚	18873558132	大专	非IT	待业	\N	深圳	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:44:46.0887+08	2024-10-21 10:48:10.744256+08	大专，铁道工程专业，24届，自家产业化工厂自动化，实习了一年，不缺钱，不想在家里干，来深圳找工作，湖南人，云南实习。	26	26	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		["云计算小视频+文字简单的概述"]	["是否想转行", "找工作有多久"]	["理性"]	32	\N
132	未知	17306535969	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:51:04.742596+08	2024-10-21 10:51:04.742612+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
113	刘玙	17385705388	本科	IT	待业	\N	哈尔滨	低	f	t	t	AI数据	f	f	0	0	2024-10-21 10:07:51.237898+08	2024-10-21 10:53:11.804045+08	大四，本科，物联网专业，南方人在哈尔滨读书，目前学校没课，在找实习，比较想去一线城市	26	26	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	盒子	[]	["找工作有多久", "是否想尽快就业", "是否了解过云计算"]	["理性"]	32	\N
134	未知	19524708717	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:53:21.905013+08	2024-10-21 10:53:21.905031+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
124	王平华	17267723843	本科	IT	待业	\N	深圳	低	f	t	t	AI数据	f	f	0	0	2024-10-21 10:34:49.555053+08	2024-10-21 10:57:50.771096+08	前年毕业，准备换工作，下个月中旬离职，准备走云和电子这一块	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	时间	[]	["是否想转行"]	["理性"]	32	\N
136	未知	18726281027	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:59:35.160584+08	2024-10-21 10:59:35.160607+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
140	未知	17691244693	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:04:12.670545+08	2024-10-21 11:04:12.67056+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
142	未知	15068259579	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:08:28.555341+08	2024-10-21 11:08:28.555356+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
144	程双妮	17789207043	大专	非IT	待业	\N	西安	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:12:31.842733+08	2024-10-21 11:12:31.84275+08	财务专业，做了5年的软件实施，刚离职，还是想往之前行业找，先了解一下	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Im	[]	["找工作有多久", "是否了解过云计算"]	[]	32	\N
146	陈宇凯	17691244693	本科	非IT	待业	\N	西安	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:15:40.928638+08	2024-10-21 11:15:40.928746+08	应届生，在西安，先加微信了解	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["找工作有多久", "是否表示工作难找"]	[]	32	\N
98	未知	00000000000	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-16 19:10:18.287743+08	2024-10-16 19:10:18.287778+08	\N	1	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
101	未知	34343434343	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-16 19:23:24.652076+08	2024-10-16 19:23:24.65209+08	\N	1	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
102	未知	88888888888	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-16 19:24:02.378015+08	2024-10-16 19:24:02.37803+08	\N	1	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
114	张怀祥	15617664305	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:08:09.370827+08	2024-10-21 10:08:09.370866+08	感兴趣，在职，前年毕业	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
106	未知	44433333322	大专	IT	待业	\N	南昌	低	f	t	f	AI数据	f	f	0	0	2024-10-16 23:18:03.83558+08	2024-10-16 23:18:03.835597+08	短发短发	1	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
107	未知	44455566677	本科	IT	待业	\N	重庆	低	f	t	t	AI数据	f	t	0	0	2024-10-16 23:23:11.240325+08	2024-10-16 23:23:11.240344+08	短发短发	1	1	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	大帅哥	[]	[]	[]	0	\N
108	未知	11144444444	大专	IT	待业	北京	南昌	低	f	t	t	视频号	f	t	0	0	2024-10-16 23:24:25.479131+08	2024-10-16 23:35:57.016685+08	个	1	1	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	大帅哥	["云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容"]	["是否表示工作难找", "找工作有多久", "是否想尽快就业", "是否想转行"]	["攻击性大", "迷茫", "墨迹"]	0	\N
109	未知	15198713513	大专	IT	待业	\N	Default City	低	f	f	f	视频号	f	f	0	0	2024-10-16 23:48:09.053776+08	2024-10-16 23:48:09.053794+08	\N	1	1	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	0	\N
118	未知	15296413550	大专	非IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:15:33.58851+08	2024-10-21 10:15:33.588524+08	20年毕业，离职找工作，会计专业	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	叶子	[]	["是否想尽快就业"]	[]	32	\N
120	未知	15683810246	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:22:19.718752+08	2024-10-21 10:22:19.718789+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
112	吴彰鑫	13758172093	未知	IT	待业	\N	重庆	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:01:26.325924+08	2024-10-21 10:25:22.373872+08	挂断	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	不知周	[]	[]	[]	32	\N
143	未知	17608896635	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:11:46.503274+08	2024-10-21 11:11:46.503289+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
116	文良丽	19065486781	大专	IT	待业	\N	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:10:43.582427+08	2024-10-21 10:28:13.077548+08	未接通	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	未知	[]	[]	[]	32	\N
5	未知	15198713510	研究生及以上	未知	未知	未知	未知	低	t	f	f	AI数据	f	f	0	0	2024-10-08 14:18:34.631235+08	2024-10-18 18:43:23.765342+08	不需要	2	1	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	0	\N
125	张宇	19863930762	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:37:22.604325+08	2024-10-21 10:37:22.604341+08	来了解云计算	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	kk	[]	[]	[]	32	\N
127	未知	15027178108	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:40:49.954641+08	2024-10-21 10:40:49.95472+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
129	未知	13814192022	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:47:06.596262+08	2024-10-21 10:47:06.596277+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
131	林鸿华	15219229773	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 10:49:31.380078+08	2024-10-21 10:49:31.380093+08	刚离职的程序员	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	抓蛙师	[]	[]	[]	32	\N
123	李志坚	19558110995	研究生及以上	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 10:33:37.163106+08	2024-10-21 10:51:21.229452+08	不接电话，加微信沟通，硕士 专业名是控制科学与工程 学的是深度学习和数据分析	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	L_	[]	[]	[]	32	\N
133	黄金鑫	19124294797	本科	IT	待业	\N	扬州	低	f	t	t	AI数据	f	f	0	0	2024-10-21 10:53:03.432242+08	2024-10-21 10:53:03.432258+08	25届软件工程去年暑假实习现在可以离校工作。实习有了解一点云计算内容。双飞本科	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Happy	[]	["找工作有多久", "是否表示工作难找", "是否了解过云计算"]	[]	32	\N
135	未知	18370498298	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 10:53:28.229293+08	2024-10-21 10:53:28.229305+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
137	未知	15310235507	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:00:15.19319+08	2024-10-21 11:00:15.193206+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
139	未知	13923911148	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:02:27.368997+08	2024-10-21 11:02:27.369012+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
141	未知	15068139913	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:08:06.557307+08	2024-10-21 11:08:06.557321+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
147	王晨	15845207171	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:15:49.71516+08	2024-10-21 11:15:49.715176+08	25届毕业生，在找实习工作	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
148	未知	17518832882	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:18:58.822572+08	2024-10-21 11:18:58.822586+08	在外面忙，加微信未通过	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
149	孙佳艺	18092621970	大专	非IT	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:19:30.780022+08	2024-10-21 11:19:30.780037+08	财务管理专业，毕业一年，不考虑云计算	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
150	谢毅飞	17707851613	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:21:30.104491+08	2024-10-21 11:21:30.104506+08	21届，专业电子信息，做通信这一块，找半个月了情况一般	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
151	未知	15214026446	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:21:34.10821+08	2024-10-21 11:21:34.108226+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
160	吴江瑶	17807942298	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:35:33.48243+08	2024-10-21 11:50:49.58527+08	25届，软件，找工作	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	吴江瑶	[]	[]	[]	32	\N
170	陈玲	18770015576	未知	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:50:41.155414+08	2024-10-21 11:51:19.072207+08	微信未回复	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	么玲	[]	[]	[]	32	\N
152	未知	15949819103	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:26:13.948608+08	2024-10-21 11:26:13.948622+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
153	吴毅	15712129661	大专	非IT	待业	\N	深圳	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:27:28.13164+08	2024-10-21 11:27:28.131731+08	之前做物业管理的，在深圳，7k的薪资，说加微信先了解	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["是否了解过云计算"]	[]	32	\N
154	未知	13349494262	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:29:51.389995+08	2024-10-21 11:29:51.390021+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
155	齐泽洲	15515025419	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:32:49.897283+08	2024-10-21 11:32:49.897297+08	25届，专业人工智能，找工作	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
156	王旭军	19394269025	未知	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:33:06.852473+08	2024-10-21 11:33:06.852488+08	在职没考虑换行，不需要	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
157	王聪聪	18790416343	本科	IT	待业	\N	杭州	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:33:56.912638+08	2024-10-21 11:33:56.912717+08	本科，学Java，做了两年，离职，之前在桂林，现在在杭州，还是比较想往java发展	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	匆聪那年	["云计算小视频+文字简单的概述"]	["找工作有多久"]	["理性"]	32	\N
159	魏俊	18460308162	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:35:24.776952+08	2024-10-21 11:35:24.776967+08	不需要	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	31	\N
161	耿士清	13753702530	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:36:14.808347+08	2024-10-21 11:36:14.808363+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	o.O	[]	[]	[]	32	\N
163	未知	18789435332	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:38:38.633971+08	2024-10-21 11:38:38.633985+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	31	\N
166	王晓波	17899316182	大专	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:42:14.260762+08	2024-10-21 11:42:14.260779+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Envy	[]	[]	[]	32	\N
162	阮丽华	15775957497	未知	未知	在职	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:37:04.040439+08	2024-10-21 11:43:35.383099+08	不考虑，不需要，挂	26	26	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
164	李启东	16626605762	本科	IT	待业	\N	广东	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:41:05.34144+08	2024-10-21 11:44:22.764232+08	明年毕业，软件工程专业，想找软件开发岗位	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	99	[]	[]	[]	32	\N
165	王桂林	15169254223	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:41:54.083291+08	2024-10-21 11:46:20.240776+08	计算机科学与技术，25届毕业找两个月，俩个面试不好找	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	羌笛吹落梅	[]	[]	[]	32	\N
168	程英明	13060925338	大专	IT	待业	\N	广东	低	f	f	f	AI数据	f	f	0	0	2024-10-21 11:44:57.442297+08	2024-10-21 11:46:22.062238+08	58岁了	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	邦联一宇	[]	[]	[]	32	\N
145	于泽	13674318435	本科	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:13:41.890436+08	2024-10-21 11:46:51.502573+08	十多年工作经验软件工程专业，做运维，找一个星期不太好找，方向运维	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Dr.Yze	[]	[]	[]	32	\N
169	郝潇灿	15133068412	本科	IT	待业	\N	兰州	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:47:07.624793+08	2024-10-21 11:50:07.07989+08	明年毕业，在兰州上学，期望就业城市江浙沪，四川	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	灿灿灿～ 🌼 🌸 🍕	[]	[]	[]	32	\N
172	路鹏达	15682072365	本科	IT	待业	\N	成都	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:55:48.845025+08	2024-10-21 11:55:48.84504+08	软件工程专业，做了3年java开发，在成都，刚离职	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["是否表示工作难找", "找工作有多久", "是否想尽快就业"]	["理性"]	32	\N
173	程成	18324996756	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:57:38.030287+08	2024-10-21 11:57:38.030301+08	在工作	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Cheasong成	[]	[]	[]	32	\N
174	熊	18174647164	本科	IT	待业	\N	长沙	低	f	t	f	AI数据	f	f	0	0	2024-10-21 12:08:25.258168+08	2024-10-21 14:11:12.143493+08	24届it想做测试不想做运维在长沙，找工作一个多月，别的城市也行，期望7-9	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	草木	[]	["是否表示工作难找", "找工作有多久", "是否想尽快就业", "是否了解过云计算"]	[]	32	\N
171	王志鹏	16627615325	本科	非IT	待业	\N	河南	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:51:43.138835+08	2024-10-21 14:14:20.1226+08	25届土木工程，有转行的想法，想在河南，没听过云计算，考了教师资格证教数学，知道工资低，先听宣讲会，问了要交费吗	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	鹏	["云计算岗位及对应的工作内容", "云计算小视频+文字简单的概述", "云计算的薪资和发展空间"]	["是否表示工作难找", "是否想转行", "是否了解过云计算", "找工作有多久", "是否想尽快就业"]	[]	32	\N
175	未知	13546855296	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:14:40.547576+08	2024-10-21 14:14:40.547592+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
158	曾	14754450042	大专	IT	待业	\N	广州	低	f	t	t	AI数据	f	f	0	0	2024-10-21 11:34:37.61972+08	2024-10-21 14:15:44.926542+08	24届卫生信息管理，刚到广州1个月住亲戚家里，在看工作，了解一点云计算	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	顺其自然	["行业的介绍（人社局-薪资、缺口、推进方向）"]	["是否表示工作难找", "找工作有多久", "是否想尽快就业", "是否了解过云计算", "是否想转行"]	[]	32	\N
122	王欣宇	15972075480	本科	IT	待业	\N	武汉黄石	低	f	t	t	AI数据	f	f	0	0	2024-10-21 10:29:49.317136+08	2024-10-21 14:18:07.256872+08	25届计算机学java学校在黄石，后面在武汉或者北上广就业	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	十四行诗	["云计算小视频+文字简单的概述"]	["是否了解过云计算"]	[]	32	\N
176	未知	18568642701	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:23:36.904615+08	2024-10-21 14:23:36.90463+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
177	未知	13416533120	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:26:03.442548+08	2024-10-21 14:26:03.442563+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
178	梁蕾	17262113615	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:26:55.463297+08	2024-10-21 14:26:55.463312+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
179	方伟壮	13380561671	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:29:18.222219+08	2024-10-21 14:29:18.222234+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	30	\N
181	未知	18775853542	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:31:10.604558+08	2024-10-21 14:31:10.604573+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
180	王建丽	15110398963	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 14:30:24.616397+08	2024-10-21 14:33:58.505781+08	不方便，微信聊	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
182	李文杰	17835884628	本科	非IT	待业	\N	石家庄	低	f	t	f	AI数据	f	f	0	0	2024-10-21 14:37:53.244462+08	2024-10-21 14:37:53.244476+08	本科，财务专业，之前做ip系统，在石家庄，待业，比较想去南方城市	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["是否想转行", "是否了解过云计算", "是否想尽快就业"]	[]	32	\N
183	未知	16630045563	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:37:59.6351+08	2024-10-21 14:37:59.635115+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
186	未知	19523135704	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 14:45:16.270299+08	2024-10-21 14:45:16.270314+08	24届待业在忙说加微信，未通过	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
187	闫康	13060480589	大专	IT	待业	\N	西安	低	f	t	t	AI数据	f	f	0	0	2024-10-21 14:47:33.43659+08	2024-10-21 14:47:33.436614+08	25届，大专，计科专业，在找工作，在西安，想往java，python，云计算这些方向去发展	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	python炒面	[]	["找工作有多久", "是否想尽快就业", "是否了解过云计算"]	["理性"]	30	\N
188	未知	13018266206	大专	IT	待业	\N	成都	低	f	t	f	AI数据	f	f	0	0	2024-10-21 14:51:55.657934+08	2024-10-21 14:51:55.657949+08	25届找实习，找了一周，随时可以离校，计算机专业，成都，实习薪资要求不高	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["找工作有多久", "是否表示工作难找", "是否想尽快就业"]	[]	32	\N
189	朱太宏	15028035427	大专	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 14:52:17.269221+08	2024-10-21 14:52:17.269235+08	大数据应届	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Red	[]	[]	[]	32	\N
184	未知	17373873127	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:41:05.16241+08	2024-10-21 14:52:31.57218+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
190	未知	19327730803	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:54:57.792377+08	2024-10-21 14:54:57.792392+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
185	洪伟杰	17381351030	研究生及以上	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 14:42:46.585937+08	2024-10-21 14:55:50.584175+08	本科计算机，研究生光计算，想往软开方向走，期望薪资15-25k	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	惊鸿 Jay Hong	[]	["是否了解过云计算"]	[]	32	\N
191	叶木秀	18688363256	未知	IT	待业	\N	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:56:28.143514+08	2024-10-21 14:57:15.206469+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
192	王羿苏	18881653201	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 14:56:39.084741+08	2024-10-21 14:58:40.506744+08	24届毕业，现在做销售，计算机专业	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	W	[]	[]	[]	32	\N
194	李仕伟	18745899616	未知	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 14:58:46.602312+08	2024-10-21 14:59:28.404362+08	不想了解	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
195	未知	15235998978	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:00:09.241995+08	2024-10-21 15:00:09.24201+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
196	未知	13518215021	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:00:42.702263+08	2024-10-21 15:00:42.702278+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
197	赵映红	18692275861	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:03:50.304256+08	2024-10-21 15:04:46.35539+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
200	Rrz	15957581826	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:13:20.401288+08	2024-10-21 15:13:20.401303+08	不感兴趣，微信还没有通过	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
201	刘长江	17631647570	未知	IT	未知	\N	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:13:53.117333+08	2024-10-21 15:13:53.117349+08	没时间参加线上宣讲会	37	37	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
167	王春喜	18220733964	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 11:42:49.362208+08	2024-10-21 15:17:34.216797+08	未接	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Laphael	[]	[]	[]	32	\N
202	于洋	17347244891	本科	非IT	待业	\N	长春	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:14:33.69704+08	2024-10-21 15:17:46.910398+08	在职，做网络优化，一本，机械自动化专业，在长春，想去南方发展，北方工资低。	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	一念丹心存一夜	["云计算小视频+文字简单的概述"]	["是否想转行", "是否了解过云计算"]	["理性"]	32	\N
203	欧阳云	18890260724	未知	IT	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:18:33.393129+08	2024-10-21 15:18:33.393144+08	找工作中	37	37	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
204	胡京雪	15205178305	研究生及以上	IT	待业	\N	南京	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:22:08.83943+08	2024-10-21 15:22:08.839444+08	电子信息硕士明年毕业了解云计算，会一些技能，在南京江浙沪都可去	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Radiant	["云计算小视频+文字简单的概述"]	["是否了解过云计算", "是否认可云计算"]	[]	32	\N
205	韩裕饶	18879338624	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:23:52.213951+08	2024-10-21 15:23:52.213966+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	琉璃	[]	[]	[]	32	\N
207	胡振宇	15838662284	大专	IT	待业	\N	合肥	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:24:32.916023+08	2024-10-21 15:24:32.916039+08	25届，计算机专业，找实习，在合肥，对工作没有一个具体方向，都行。	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	["迷茫"]	32	\N
193	韩驰	18317729100	大专	IT	待业	\N	北方	低	f	t	t	AI数据	f	f	0	0	2024-10-21 14:57:45.818212+08	2024-10-21 15:24:58.022255+08	24届，计算机专业，北方人，想往南方发展，在家呆了一段时间刚找工作	26	26	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	喜洋洋	[]	["是否了解过云计算", "找工作有多久"]	[]	32	\N
208	未知	19577728407	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:25:25.058451+08	2024-10-21 15:25:25.058465+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
206	符常宇	13692460651	本科	IT	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:24:13.704965+08	2024-10-21 18:04:46.705616+08	学计算专业的	35	35	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	考拉饲养员	[]	["是否了解过云计算"]	[]	32	\N
198	啦啦啦	18894136380	本科	未知	在职	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:09:13.462003+08	2024-10-21 18:06:40.094889+08	先加微信，做个亚马逊运营现在在要做五金采购一个月要出差20天，刚毕业4个月	36	36	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	啦啦啦	[]	[]	[]	32	\N
210	郑丁	15172328361	大专	IT	待业	\N	深圳	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:32:53.829616+08	2024-10-21 15:32:53.829631+08	会计来了解云计算	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	审计小邓	[]	["是否想转行"]	[]	32	\N
211	未知	13997553101	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:35:08.444529+08	2024-10-21 15:35:08.444544+08	\N	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
212	未知	18254796254	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:35:32.257742+08	2024-10-21 15:35:32.257764+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
214	未知	18382715071	大专	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:39:45.797716+08	2024-10-21 15:42:08.559116+08	一直说不用不用	36	36	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
215	肖雯	18390357886	本科	IT	待业	\N	长沙	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:43:42.820871+08	2024-10-21 15:43:42.8209+08	25届软件工程投java本科长沙	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	不思議さん	[]	["是否表示工作难找", "找工作有多久", "是否想尽快就业", "是否了解过云计算"]	[]	32	\N
216	郭启宁	13220040269	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:44:49.631406+08	2024-10-21 15:44:49.63142+08	25届，计算机科学，还有一个月结束课程，找实习	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	且陶陶	[]	[]	[]	32	\N
217	未知	15903655327	大专	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:45:27.106591+08	2024-10-21 15:46:08.89569+08	不考虑	36	36	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
218	罗旺	13398296508	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:49:52.145171+08	2024-10-21 15:49:52.145186+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
232	熊一帆	18827627866	未知	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:03:46.319143+08	2024-10-21 16:03:46.319156+08	未接	35	35	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
220	未知	18393500508	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:50:23.184763+08	2024-10-21 15:50:23.184787+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
221	未知	18338183374	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:51:24.337163+08	2024-10-21 15:51:24.337178+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
219	李世栋	15386904930	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:49:57.764204+08	2024-10-21 15:52:25.330013+08	21届毕业，在职运维想换工作，专业软件	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	李	[]	[]	[]	32	\N
213	邵越	15681552928	研究生及以上	IT	待业	\N	成都	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:39:43.511362+08	2024-10-21 15:52:27.109378+08	24届，研究生，计算机专业，在成都，自己对测试比较感兴趣，可以先了解一下	26	26	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	凶巴巴呛扁扁怪兽	[]	[]	[]	32	\N
222	未知	15561838321	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:53:29.404757+08	2024-10-21 15:53:29.404779+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
223	未知	13557333088	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:54:56.69428+08	2024-10-21 15:54:56.694296+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
224	李李	15107279325	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:57:13.327958+08	2024-10-21 15:57:35.298989+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
226	小邓	18574687708	大专	IT	待业	\N	扬州	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:58:29.511535+08	2024-10-21 15:58:29.511549+08	24届计科周三线上面试，在扬州想去深圳广州长沙，投后端岗位	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	kh	[]	["找工作有多久", "是否表示工作难找", "是否想尽快就业", "是否了解过云计算"]	[]	32	\N
225	吴庆祥	18770003742	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:57:59.590237+08	2024-10-21 15:58:31.703624+08	不需要没兴趣	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
228	苗根培	13460655929	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:00:02.951127+08	2024-10-21 16:00:02.951141+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Conba	[]	[]	[]	32	\N
227	张义博	15342257619	本科	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-21 15:58:54.431965+08	2024-10-21 16:01:27.175284+08	目前还是想往测试方向发展	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	藤原拓海🌊	[]	[]	[]	32	\N
230	黄凌斌	15108375124	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:01:56.417498+08	2024-10-21 16:01:56.417513+08	25届，找实习，比较想从事软件开发	37	37	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	我為我心	[]	[]	[]	32	\N
233	未知	17360062993	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:05:03.906373+08	2024-10-21 16:05:03.906388+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
234	陈永昆	13168042246	未知	IT	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:06:48.792875+08	2024-10-21 16:06:48.792889+08	19年毕业	37	37	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	綝郴.	[]	[]	[]	29	\N
235	邢锦双	18591958920	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:11:00.216284+08	2024-10-21 16:11:00.216299+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
236	未知	19102690195	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:11:28.637724+08	2024-10-21 16:11:28.637758+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
237	武恒毅	15698473896	未知	IT	待业	\N	山西	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:13:59.192746+08	2024-10-21 16:13:59.192761+08	25届，找实习，离家近	37	37	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
238	谢成锟	13822501987	大专	IT	待业	\N	深圳	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:14:29.486801+08	2024-10-21 16:14:29.486814+08	20年毕业，离职，之前学计算机的，目前在省武协兼职，在找工作，测开方向	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	kk	[]	["找工作有多久", "是否想尽快就业"]	[]	32	\N
239	刘源	17620878311	本科	IT	待业	\N	深圳	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:17:41.753399+08	2024-10-21 16:17:41.753413+08	本科，java，做了8年，之前部门解散，在深圳	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["找工作有多久", "是否表示工作难找"]	["理性"]	32	\N
241	未知	13022982747	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:18:56.911102+08	2024-10-21 16:18:56.911118+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
209	K.L	19109600964	大专	IT	待业	\N	杭州	低	f	f	f	AI数据	f	f	0	0	2024-10-21 15:29:07.924894+08	2024-10-22 16:23:25.246852+08	加微信，学计算机的 24年毕业的，在北京实习的，目前在杭州	36	36	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	K.L	[]	[]	[]	32	\N
229	秦章真	17883479057	本科	IT	待业	\N	四川	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:01:53.775382+08	2024-10-21 17:52:50.684845+08	毕业一年，之前做维修，考虑换行业发展，对云计算没什么了解	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	t	f	一般	A对方正在输入...	[]	[]	[]	32	\N
242	王树鹤	19967346488	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:21:06.473887+08	2024-10-21 16:21:06.473917+08	在外面忙，加微信，之前做软件开发，离职了	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
243	未知	13385584568	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:22:04.200264+08	2024-10-21 16:22:04.200278+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
240	黄一晋	15889944553	本科	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:18:32.362221+08	2024-10-21 16:23:27.78714+08	25届，找工作计算机	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
245	周跃发	18085971654	大专	未知	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:23:56.894828+08	2024-10-21 16:23:56.894843+08	在微信上已经沟通过了	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	t	f	一般	拟发	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	["找工作有多久", "是否想尽快就业", "是否了解过云计算"]	[]	32	\N
246	张恒瑞	13550166643	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:25:04.632498+08	2024-10-21 16:25:04.632533+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
247	朱霆邦	19071456705	大专	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:26:05.385895+08	2024-10-21 16:26:05.385911+08	微信上进行沟通了解	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	t	f	一般	Camellia	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	["是否了解过云计算"]	[]	32	\N
244	屈辉辉	17691395548	本科	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:22:27.572+08	2024-10-21 16:26:47.469356+08	16届毕业，机电，培训计算机，离职一个月找工作，之前在华为云做外包	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	7阿辉	[]	[]	[]	32	\N
250	杨谊萍	15129588098	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:26:55.484406+08	2024-10-21 16:26:55.484423+08	微信上进行沟通了解	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	她好漂亮	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
251	赵海龙	13018079796	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:29:27.739495+08	2024-10-21 16:29:27.73951+08	微信上进行沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	绅士。	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
252	未知	15681085716	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:30:36.450322+08	2024-10-21 16:30:36.450344+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
253	未知	15013951745	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:31:11.351371+08	2024-10-21 16:31:11.351386+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
254	未知	15719639302	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:31:23.341024+08	2024-10-21 16:31:23.341038+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
255	萨姆	15621872132	研究生及以上	非IT	待业	\N	大连	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:32:53.393431+08	2024-10-21 16:32:53.393446+08	肃甘人，少数名族，土木工程专业，大连理工大学，研究生在读，25年毕业，	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
256	未知	15770620570	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:33:01.369308+08	2024-10-21 16:33:01.369329+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
257	徐林	15823475716	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:33:28.234109+08	2024-10-21 16:33:28.234124+08	微信上进行沟通了	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	XX	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
258	周航亦	15675833542	未知	非IT	待业	\N	湖南	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:33:59.967796+08	2024-10-21 16:33:59.96782+08	应届生，工程专业，想在广东找工作	37	37	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	瓜皮	[]	[]	[]	32	\N
259	董燕鼎	17719098747	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:34:27.634788+08	2024-10-21 16:34:27.634804+08	微信上进行沟通了解	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	小夏	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
260	罗文龙	15978305683	大专	IT	待业	\N	西安	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:34:37.96852+08	2024-10-21 16:34:37.968536+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
261	未知	18336110212	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:34:41.862425+08	2024-10-21 16:34:41.86244+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
262	未知	13915484208	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:34:57.939096+08	2024-10-21 16:34:57.939111+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
263	张佳晨	18629392087	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:36:06.605607+08	2024-10-21 16:36:06.605634+08	微信上进行沟通了解	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	sunrise	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
264	樊有亮	17807067971	未知	未知	在职	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:37:54.95467+08	2024-10-21 16:37:54.954689+08	在职，不太想沟通，到时候再看	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
265	未知	13220015892	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:38:13.872321+08	2024-10-21 16:38:13.872337+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
266	未知	13362895295	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:38:41.448933+08	2024-10-21 16:38:41.448947+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
248	未知	17825528363	未知	未知	未知	\N	未知	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:26:36.638337+08	2024-10-21 18:15:00.264476+08	\N	35	35	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
267	未知	18966875975	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:39:29.136574+08	2024-10-21 16:39:29.136589+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
268	池卓逸	18876423531	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:40:42.952736+08	2024-10-21 16:40:42.952774+08	微信上沟通详情	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	下雨了🌂	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
270	潘玲雅	18858957939	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:41:25.611955+08	2024-10-21 16:41:25.61197+08	微信上沟通了解	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	清浅	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
271	未知	17340966696	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:41:36.711976+08	2024-10-21 16:41:36.711993+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
272	未知	15037728540	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:41:49.007497+08	2024-10-21 16:41:49.007511+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
273	李峰	18893781167	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:42:36.512301+08	2024-10-21 16:42:36.512317+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Lf	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
274	未知	17735410907	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:42:50.449451+08	2024-10-21 16:42:50.449466+08	\N	27	27	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
275	程一豪	18537225793	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:43:23.090255+08	2024-10-21 16:43:23.090274+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	聿怀	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
276	未知	13670214882	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:43:59.592847+08	2024-10-21 16:43:59.592862+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
277	空白	16607478010	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:44:04.116485+08	2024-10-21 16:44:04.1165+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Rebirth	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
278	潘俊尧	18051218812	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:44:43.977127+08	2024-10-21 16:44:43.97714+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	阿潘	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
280	未知	19162048097	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:44:53.276909+08	2024-10-21 16:44:53.276924+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
281	穆大诚	18538389760	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:45:55.352193+08	2024-10-21 16:45:55.352219+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	古城	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
282	未知	15353768502	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:46:05.69518+08	2024-10-21 16:46:05.695207+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
283	未知	18748620727	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:46:15.636942+08	2024-10-21 16:46:15.636956+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
284	未知	18876718729	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:46:25.761907+08	2024-10-21 16:46:25.761922+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
285	未知	18463731769	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:46:30.944224+08	2024-10-21 16:46:30.944238+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
286	曾美香	13319469831	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:47:26.187136+08	2024-10-21 16:47:26.187151+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	十大混蛋啊	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
287	未知	18634785675	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:47:39.293315+08	2024-10-21 16:47:39.293331+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
288	未知	16638397384	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:47:49.302365+08	2024-10-21 16:47:49.30238+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
289	空白	18038549982	未知	未知	未知	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:48:39.912482+08	2024-10-21 16:48:39.912498+08	微信沟通	25	25	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	一个符号	["云计算小视频+文字简单的概述", "云计算有几种服务模式（服务模式对应的场景）", "云计算的薪资和发展空间", "云计算岗位及对应的工作内容", "云计算和数字经济的关联性", "行业的介绍（人社局-薪资、缺口、推进方向）"]	[]	[]	32	\N
290	未知	19301171729	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:48:49.597851+08	2024-10-21 16:48:49.597866+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
291	未知	13653861964	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:49:00.64203+08	2024-10-21 16:49:00.642044+08	\N	25	25	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
269	王	17609243275	大专	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:41:07.212359+08	2024-10-21 18:12:47.227952+08	失业状态，计算机专业，做过运维工作	35	35	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	capy	[]	[]	[]	32	\N
292	李杰	17639853551	本科	非IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:51:09.924445+08	2024-10-21 16:51:09.924459+08	24届，材料学找工作	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
293	刘鑫	17526369332	未知	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:59:40.179915+08	2024-10-21 16:59:40.17993+08	24届，软件专业，想从事开发类	37	37	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	.	[]	[]	[]	32	\N
294	王家豪	15816573371	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:02:18.530251+08	2024-10-21 17:02:18.530267+08	待业	26	26	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	路垚.	[]	[]	[]	32	\N
296	未知	18549826732	大专	非IT	待业	\N	杭州	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:03:25.11032+08	2024-10-21 17:03:25.110334+08	23届高铁相关专业，做物流之前，一直夜班离职了，大专在杭州	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	["找工作有多久", "是否想尽快就业"]	[]	32	\N
279	郑锐松	13727936536	大专	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 16:44:48.785912+08	2024-10-21 17:03:39.207359+08	24届，计算机专业，之前做设备实体运维，离职，在开车，加微信聊	26	26	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Z	[]	[]	[]	32	\N
297	未知	19806937326	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:03:57.682192+08	2024-10-21 17:03:57.682206+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
298	未知	16769704083	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:06:43.688944+08	2024-10-21 17:06:43.688958+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
302	未知	15524430773	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:09:36.212954+08	2024-10-21 17:09:36.21297+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
249	黎小姐	15913226950	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 16:26:39.991877+08	2024-10-21 17:10:38.761632+08	\N	26	26	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
305	未知	13060447531	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:15:57.694358+08	2024-10-21 17:15:57.694371+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
304	谭毅龙	18373273602	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:14:39.762741+08	2024-10-21 17:16:10.754885+08	\N	37	37	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
303	郭开天	18678600340	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:14:20.412941+08	2024-10-21 17:16:53.664435+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
307	吴佳佳	19165821231	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:19:25.417623+08	2024-10-21 17:20:26.345325+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
308	陈泽鹏	13246764123	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:21:36.163979+08	2024-10-21 17:22:22.685346+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
309	李鹏	18581591025	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:22:34.82545+08	2024-10-21 17:22:34.825464+08	计科专业，先加微信了解	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
310	未知	13610525113	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:22:37.113202+08	2024-10-21 17:22:37.113217+08	\N	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
312	未知	19936040638	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:24:31.709592+08	2024-10-21 17:24:31.709607+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	31	\N
306	未知	13198260853	本科	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:18:50.997058+08	2024-10-21 17:29:43.576005+08	找工作	22	22	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
315	未知	13251370833	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:31:00.015403+08	2024-10-21 17:31:00.015434+08	\N	37	37	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	30	\N
316	杜林彬	15216152454	大专	IT	待业	\N	南昌	低	f	t	t	AI数据	f	f	0	0	2024-10-21 17:31:44.251139+08	2024-10-21 17:31:44.251155+08	22年离职，之前做开发，找工作一个多月，在南昌	27	27	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	joker	["云计算小视频+文字简单的概述", "云计算的薪资和发展空间"]	["是否表示工作难找", "找工作有多久", "是否想尽快就业", "是否了解过云计算"]	[]	32	\N
295	李程鹏	15135630821	本科	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:03:09.861041+08	2024-10-21 17:57:45.970464+08	25届找实习通信工程	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Dimensionit	[]	[]	[]	32	\N
300	斯潮杰	18815012635	大专	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 17:07:32.665367+08	2024-10-21 17:32:26.323871+08	找工作一俩月，信息专业	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	小斯不听话	[]	[]	[]	32	\N
319	匡志	18587932860	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:47:37.811739+08	2024-10-21 17:48:29.975873+08		2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
313	未知	13209446828	本科	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 17:27:06.136632+08	2024-10-21 17:34:21.753512+08	24届物联网找工作	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	路人甲	[]	[]	[]	32	\N
317	未知	15144105363	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:41:26.652905+08	2024-10-21 17:41:26.652921+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
320	未知	15014803223	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:49:02.502992+08	2024-10-21 17:49:02.503006+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
322	王宏伟	15095796768	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:50:11.091365+08	2024-10-21 17:50:57.480119+08	这会在忙，晚点通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
323	彭帅	18871433244	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:51:40.898239+08	2024-10-21 17:52:28.828862+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
318	曹佳怡	17693810823	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:43:33.046458+08	2024-10-21 18:02:15.121775+08	先加微信后续再慢慢跟进	36	36	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Oyggnik	[]	[]	[]	32	\N
321	肖	18473433572	大专	IT	待业	\N	永州	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:49:20.089776+08	2024-10-21 18:10:07.60299+08	计算机专业的，大专，大三，还没有找实习工作，对未来的发展没有思考过，打算专升本	35	35	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	礼	[]	[]	[]	32	\N
311	未知	13759672435	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:23:41.273633+08	2024-10-21 18:13:13.032903+08	打电话有点忙，所以加微信，还未通过	35	35	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
299	未知	17395715631	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:06:51.972419+08	2024-10-21 18:13:31.834539+08	\N	35	35	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
314	王女士	15618562669	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:29:46.833594+08	2024-10-21 18:14:29.162825+08	有点忙，加微信未通过	35	35	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
388	未知	19146894029	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 17:15:56.557121+08	2024-10-22 17:16:13.164315+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
324	杨丙坤	17511635283	大专	非IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:52:13.335373+08	2024-10-21 17:52:13.335388+08	15年学习过，在北京但是没有推荐就业	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
325	陆聖	18667365098	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:52:22.052081+08	2024-10-21 17:52:22.052097+08	在忙，先加微信了解	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
301	未知	13790703771	未知	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:08:04.40917+08	2024-10-21 17:54:40.418028+08		26	26	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
326	江汉威	18420426145	未知	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:56:25.106551+08	2024-10-21 17:56:25.106566+08	对云计算不了解，兴趣不是很大，可以先加微信，待通过	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
328	未知	17686682957	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:57:31.116246+08	2024-10-21 17:57:31.116262+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
327	王紫阳	15594903532	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:56:40.446192+08	2024-10-21 17:57:31.752262+08	没兴趣	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
329	未知	18770602220	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 17:58:17.680382+08	2024-10-21 17:58:17.680397+08	加微信，在上班后续慢慢跟进	36	36	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Bright	[]	[]	[]	32	\N
330	未知	18689638936	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 17:58:42.567602+08	2024-10-21 17:58:42.567617+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
332	未	18922663968	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 18:02:47.650733+08	2024-10-21 18:02:47.650788+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	知	[]	[]	[]	32	\N
333	谭杰	18273010583	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:03:35.85961+08	2024-10-21 18:03:54.448087+08	重复数据	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
335	蓝淇峰	15220996093	未知	非IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 18:06:25.39046+08	2024-10-21 18:06:25.390475+08	对云计算了解不多，有兴趣了解，先加微信	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
334	祁宏祥	15340778461	本科	IT	待业	\N	山西	低	f	t	t	AI数据	f	f	0	0	2024-10-21 18:05:23.274464+08	2024-10-21 18:11:21.556904+08	学大数据，对云计算有了解过，想进国企，明年毕业	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	玄	[]	[]	[]	32	\N
345	未知	19829140829	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:18:38.476338+08	2024-10-21 18:18:38.476352+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
336	夏伊蕊	15639573035	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:12:07.21483+08	2024-10-21 18:12:31.358383+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
338	未知	17788461095	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:13:50.063335+08	2024-10-21 18:13:50.063351+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
337	未知	18034940742	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:13:45.131604+08	2024-10-21 18:14:22.575863+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
339	未知	18168271770	大专	IT	待业	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 18:15:14.93803+08	2024-10-21 18:15:14.938043+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	小kun	[]	[]	[]	32	\N
341	何鹏	18388530879	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 18:16:02.593312+08	2024-10-21 18:16:02.593327+08	不需要	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
331	未知	17550238265	本科	IT	待业	\N	Default City	低	f	t	t	AI数据	f	f	0	0	2024-10-21 18:01:38.815488+08	2024-10-21 18:16:21.563547+08	24届计算机科学	22	22	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Playmaker	[]	[]	[]	32	\N
340	未知	15836685879	大专	非IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-21 18:15:45.46704+08	2024-10-21 18:16:51.763226+08	学土木，薪资在5k左右，再考虑转行，先观望一下	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	诸事皆宜	[]	[]	[]	32	\N
343	未知	13169368421	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:17:26.341828+08	2024-10-21 18:17:26.341842+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
342	未知	15815364482	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:17:25.579173+08	2024-10-21 18:18:05.373564+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
344	未知	17680588251	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:18:32.065258+08	2024-10-21 18:19:08.06607+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
346	朱伟豪	19914529276	本科	IT	待业	\N	Default City	低	f	t	t	AI数据	f	f	0	0	2024-10-21 18:20:15.320177+08	2024-10-21 18:22:04.598807+08	做过Java，对云计算有一定了解，先了解一下	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	情汐	[]	[]	[]	32	\N
231	心火	17855680210	未知	未知	未知	\N	上海	低	f	t	f	AI数据	f	f	0	0	2024-10-21 16:02:41.551172+08	2024-10-21 18:26:23.603802+08	加微信，想从事嵌入式软件方向工作	36	36	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	心火	["云计算小视频+文字简单的概述"]	["是否了解过云计算", "是否想转行", "是否表示工作难找"]	[]	32	\N
347	张开兴	13281556626	大专	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-21 18:30:30.969606+08	2024-10-21 18:30:30.96962+08	1	6	6	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	ⁱ	[]	[]	[]	32	\N
348	未知	18148955146	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:31:04.434013+08	2024-10-21 18:31:04.434028+08	\N	6	6	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
349	未知	15673038477	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-21 18:33:27.023973+08	2024-10-21 18:33:27.023987+08	\N	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	31	\N
350	钟泽朝	16624798579	未知	未知	未知	\N	东莞	低	f	t	f	AI数据	f	f	0	0	2024-10-21 18:36:12.51618+08	2024-10-21 18:36:12.516194+08	在吃饭，先加微信了解	4	4	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	31	\N
352	廖	17673399912	未知	IT	待业	\N	广州	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:34:15.22763+08	2024-10-22 10:34:15.227725+08	刚毕业，在长沙做的软件测试的实习工作，现在去广州找工作，还在找工作的状态	35	35	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	橘络	[]	[]	[]	32	\N
353	未知	15237324981	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:39:03.32936+08	2024-10-22 10:39:03.329397+08	先加微信沟通，暂时不方便	34	34	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
354	魏杰	18239625623	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:41:21.70402+08	2024-10-22 10:41:21.704034+08	直接说不用	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
199	段阳帆	17386472750	未知	IT	在职	\N	未知	低	f	t	t	AI数据	f	f	0	0	2024-10-21 15:10:58.481932+08	2024-10-22 11:38:16.070955+08	学物联网的，实习工作做过汽车座椅控制，未来的就业方向是嵌入式，软件方面的，没进群，把我删了	35	35	t	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	1	[]	[]	[]	32	\N
351	陈	19120556321	未知	IT	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:24:53.201361+08	2024-10-22 10:42:09.42859+08	客户计算机的工作2-3年了，被删了	36	36	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	duh	[]	[]	[]	32	\N
355	未知	18007060176	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:44:37.476528+08	2024-10-22 10:44:37.476542+08	微信沟通	18	18	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	呆呆的高冷鱼	[]	[]	[]	32	\N
356	黑化肥会挥发	15838334013	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:49:02.153413+08	2024-10-22 10:49:02.153429+08	先加微信慢慢沟通	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
357	未知	13038543913	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 10:50:47.635319+08	2024-10-22 10:50:47.635334+08	\N	18	18	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
358	张宏图	15256703799	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 10:56:48.035954+08	2024-10-22 10:56:48.035969+08	直接挂	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
359	linux	13729333136	未知	IT	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:02:01.871903+08	2024-10-22 11:02:01.871918+08	不方便，先加微信	34	34	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
360	未知	17746321561	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:05:20.761345+08	2024-10-22 11:05:20.761359+08	\N	18	18	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
361	啊	15537793552	未知	未知	待业	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:10:40.37051+08	2024-10-22 11:10:40.370524+08	先加微信后续跟进	36	36	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
362	未知	18333618705	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:13:13.833983+08	2024-10-22 11:13:13.833999+08	微信沟通	18	18	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	阿祖	[]	[]	[]	32	\N
363	未知	18181579085	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:15:54.519697+08	2024-10-22 11:15:54.51972+08	\N	35	35	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
364	未知	13142947619	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:16:12.856186+08	2024-10-22 11:16:12.856201+08	\N	18	18	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
365	未知	17547532545	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:24:21.196971+08	2024-10-22 11:24:21.196985+08	微信沟通	18	18	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	🍊	[]	[]	[]	32	\N
366	未知	18989557918	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:32:05.151049+08	2024-10-22 11:32:05.151063+08	微信沟通	18	18	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	。	[]	[]	[]	32	\N
368	未知	18270686334	未知	未知	未知	\N	未知	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:38:09.970923+08	2024-10-22 11:38:09.970937+08	微信沟通	18	18	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	弋	[]	[]	[]	32	\N
367	李茂洋	19130204820	本科	IT	待业	\N	四川	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:37:00.608511+08	2024-10-22 11:38:43.443157+08	未通过微信	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Apricity	[]	[]	[]	32	\N
370	未知	13434126800	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:40:05.87486+08	2024-10-22 11:40:05.874875+08	\N	18	18	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
371	未知	15303284877	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:40:53.25213+08	2024-10-22 11:40:53.252161+08	\N	18	18	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
369	朱晶	17873464210	大专	IT	待业	\N	深圳	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:39:41.350976+08	2024-10-22 11:42:36.904848+08	微信未回复	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	海星	[]	[]	[]	32	\N
372	刘恋	18186327373	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:43:10.516835+08	2024-10-22 11:43:36.445383+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
373	张迎春	18389586327	本科	IT	在职	\N	海南	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:44:06.490498+08	2024-10-22 11:45:42.763029+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
374	洪志强	18374826192	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:46:15.94709+08	2024-10-22 11:46:43.304756+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
375	詹友生	15886484130	本科	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:47:14.156899+08	2024-10-22 11:48:18.271797+08	微信未回复	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	@	[]	[]	[]	32	\N
376	陈昱桥	18946401962	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:48:41.123502+08	2024-10-22 11:49:09.521913+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
377	徐映江	13417504910	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:49:37.235395+08	2024-10-22 11:50:24.372022+08	微信未回复	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	徐映江	[]	[]	[]	32	\N
378	郭棚伟	16650032419	本科	IT	待业	\N	河南	低	f	t	f	AI数据	f	f	0	0	2024-10-22 11:50:51.223604+08	2024-10-22 11:52:37.478394+08	应届毕业生，物联网应用技术，找本专业工作感觉比较难	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	呆o_	[]	[]	[]	32	\N
379	杨春	15277106070	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 11:53:39.194521+08	2024-10-22 11:54:09.838862+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
380	未知	17621154120	本科	非IT	在职	\N	杭州	低	f	t	f	AI数据	f	f	0	0	2024-10-22 14:35:50.755132+08	2024-10-22 14:39:44.751356+08	工商类，目前在职工资不高，对云计算没了解过，先了解一下	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	唱花旦的角儿	[]	[]	[]	32	\N
381	未知	13868113745	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 14:40:14.7086+08	2024-10-22 14:40:33.480302+08	没兴趣，不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
382	未知	13033994511	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 14:40:59.302584+08	2024-10-22 14:41:12.16001+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
383	未知	15709296481	大专	IT	待业	\N	陕西	低	f	f	f	AI数据	f	f	0	0	2024-10-22 14:59:29.575543+08	2024-10-22 15:00:10.633976+08	挂断	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
384	未知	18144063396	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 17:05:56.77038+08	2024-10-22 17:06:12.474387+08	没兴趣	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
386	崔伟	15645995613	研究生及以上	IT	待业	\N	上海	低	f	t	t	AI数据	f	f	0	0	2024-10-22 17:09:55.172895+08	2024-10-22 17:28:47.876249+08	对计算机行业比较感兴趣，在云计算公司实习过，在上海期望薪资1.6-1.8	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	原点	[]	[]	[]	32	\N
387	徐森	15919910937	本科	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-22 17:11:13.733086+08	2024-10-22 17:15:22.627539+08	毕业很多年，之前做软件测试，行情不太好，对云计算了解还是比较多	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Johnson	[]	[]	[]	32	\N
385	郝阳	15795761501	本科	IT	待业	\N	上海	低	f	t	f	AI数据	f	f	0	0	2024-10-22 17:06:53.507978+08	2024-10-22 17:26:29.432742+08	微信未回复	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	泽泽	[]	[]	[]	32	\N
389	张	13033121161	大专	非IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-22 17:16:57.913329+08	2024-10-22 17:20:08.218413+08	应用统计学，先了解一下行业	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	Weirdo :)	[]	[]	[]	32	\N
390	未知	18278690641	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 17:21:00.701465+08	2024-10-22 17:21:00.70148+08	\N	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	\N	[]	[]	[]	32	\N
391	未知	15895901903	本科	IT	待业	\N	江苏	低	f	f	f	AI数据	f	f	0	0	2024-10-22 17:52:07.381271+08	2024-10-22 17:52:42.509838+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
392	未知	19170877112	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 17:53:12.051793+08	2024-10-22 17:53:54.298922+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
393	未知	19396711810	大专	IT	待业	\N	Default City	低	f	f	f	视频号	f	f	0	0	2024-10-22 17:59:20.420081+08	2024-10-22 17:59:44.894814+08	不需要，已经找到工作了	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
394	未知	15289580574	本科	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-22 18:01:47.784178+08	2024-10-22 18:02:10.210185+08	微信未回复	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
395	李	18916602475	大专	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-22 18:11:13.104797+08	2024-10-22 18:11:40.90753+08	微信未回复	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	我是ꦿ࿐李行七分倔强牵强᭄	[]	[]	[]	32	\N
396	陈	15817044245	大专	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-23 10:44:51.5336+08	2024-10-23 10:46:46.369278+08	微信被删	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	℡	[]	[]	[]	32	\N
397	王鑫洋	18906418776	本科	IT	待业	\N	国外	低	f	t	t	AI数据	f	f	0	0	2024-10-23 11:03:49.599495+08	2024-10-23 11:05:10.521723+08	软件技术相关专业，目前在国外，想往技术方面发展	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	咕哒子botshea	[]	[]	[]	32	\N
398	杨应科	18483541480	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 11:05:34.878548+08	2024-10-23 11:05:56.355102+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
399	未知	17674668669	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 11:28:01.794546+08	2024-10-23 11:28:25.02807+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
400	未知	13417121559	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 11:29:52.608855+08	2024-10-23 11:30:24.950876+08	在忙，稍后通过微信	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
401	周松林	17772376070	大专	IT	待业	\N	西安	低	f	f	f	AI数据	f	f	0	0	2024-10-23 11:31:12.255016+08	2024-10-23 11:31:51.312181+08	没兴趣	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
402	李思雨	18239175791	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 11:32:14.534484+08	2024-10-23 11:32:37.444479+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
403	李绍兵	15133055991	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:07:47.174437+08	2024-10-23 15:08:23.012327+08	微信未通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	yes	[]	[]	[]	32	\N
404	耿家良	18061230709	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:08:48.962988+08	2024-10-23 15:09:17.968608+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
405	刘童辉	17829916352	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:10:59.077509+08	2024-10-23 15:11:40.613285+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
406	未知	15216031712	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:12:20.860885+08	2024-10-23 15:12:31.218815+08	\N	2	2	t	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
407	未知	15871753806	研究生及以上	IT	待业	\N	上海	低	f	t	f	AI数据	f	f	0	0	2024-10-23 15:12:57.297769+08	2024-10-23 15:15:20.363373+08	毕业两年，在上海，掌握一些基础命令，了解过费用	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	使徒行者	[]	["是否有知识付费的意识"]	[]	32	\N
408	未知	15969402417	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:16:00.648769+08	2024-10-23 15:16:11.916897+08	挂断	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
409	江晓鹏	15779497728	本科	IT	待业	\N	Default City	低	f	t	f	AI数据	f	f	0	0	2024-10-23 15:17:33.649186+08	2024-10-23 15:20:50.133166+08	应届毕业，去年十月份实习到九月离职，做软件开发，想进一步发展	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
410	李杰深	15217813847	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:21:18.42083+08	2024-10-23 15:21:47.661495+08	挂断	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
411	钟	18128694557	本科	IT	待业	\N	东莞	低	f	t	t	AI数据	f	f	0	0	2024-10-23 15:40:33.267782+08	2024-10-23 15:42:32.153408+08	毕业三年，做安全类前端开发，想在深圳发展，期望薪资10k	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	-	[]	[]	[]	32	\N
412	未知	19065378879	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:45:25.263401+08	2024-10-23 15:46:51.609058+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
413	未知	15085347056	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:47:31.259584+08	2024-10-23 15:47:45.842409+08	微信待通过	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
414	侯真龙	19512251264	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:57:58.447871+08	2024-10-23 15:58:22.052451+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
415	唐杰	15681560023	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 15:59:29.615903+08	2024-10-23 15:59:53.888764+08	微信未回复	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
416	杨尧	18973152880	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 16:00:17.407996+08	2024-10-23 16:00:40.958157+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
417	韩文超	18941040686	本科	IT	待业	\N	深圳	低	f	t	t	AI数据	f	f	0	0	2024-10-23 16:01:05.313395+08	2024-10-23 16:03:23.273623+08	25届毕业生，期望薪资6-8k在深圳	2	2	f	t	f	f	f	\N	f	\N	f	\N	一般	f	f	一般	CUA～	[]	[]	[]	32	\N
418	未知	15692294014	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 16:21:20.118263+08	2024-10-23 16:21:30.298625+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
419	未知	18800325072	本科	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 16:54:35.156225+08	2024-10-23 16:54:56.635833+08	在忙，稍后通过微信	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
420	刘辉	16673192533	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 16:55:20.579019+08	2024-10-23 16:55:37.857364+08	没兴趣	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
421	李文健	13288125023	本科	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 16:56:04.515523+08	2024-10-23 16:56:56.088859+08	34岁了不想转行，在广州做前端	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
422	邵	13176743342	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 17:51:28.572187+08	2024-10-23 17:52:17.399552+08	不需要	2	2	f	f	f	f	f	\N	f	\N	f	\N	一般	f	f	一般		[]	[]	[]	32	\N
6	彭	18836195805	研究生及以上	IT	待业	郑州	郑州	中	f	t	f	AI数据	f	f	0	0	2024-10-08 14:20:39.294594+08	2024-11-02 09:47:35.532862+08	刚毕业，期望薪资七八千，之前干Java，找工作一个多月	2	1	t	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	0	大师比
431	未知	33333333333	大专	IT	待业	\N	Default City	未知	f	f	f	AI数据	f	f	0	0	2024-11-02 10:37:45.882946+08	2024-11-02 10:37:45.882961+08		1	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	["option1"]	["option2"]	["option3"]	0	
432	大傻逼	1234567890	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-11-02 10:39:58.496394+08	2024-11-02 10:40:09.452309+08		1	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	0	大傻逼
428	未知	18375519693	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 18:11:03.702209+08	2024-11-11 21:36:00.110137+08	不需要	2	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	32	客户忍耐
427	未知	18389573873	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 18:10:30.678246+08	2024-11-11 22:00:24.005466+08		2	1	t	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	32	大傻逼
425	未知	13670035357	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 18:08:27.600359+08	2024-11-11 22:12:16.020261+08	挂断	2	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	30	再追
423	陈秒烨	17376360535	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 17:55:27.120939+08	2024-11-11 22:20:35.632228+08	微信未通过	2	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	32	大傻逼
424	未知	15076899625	大专	IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 17:57:33.915254+08	2024-11-11 22:33:42.269759+08	不需要	2	1	f	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	32	猪头
426	小文	17304516373	本科	非IT	待业	\N	Default City	低	f	f	f	AI数据	f	f	0	0	2024-10-23 18:09:12.978551+08	2024-11-11 22:40:35.042542+08	学食品科学，不需要了	2	1	f	t	f	f	f		f		f		一般	f	f	一般	。。	[]	[]	[]	32	大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方大地方
434	未知	11144444444	大专	IT	待业	\N	Default City	低	f	f	f	视频号	f	f	0	0	2024-11-11 22:42:27.056358+08	2024-11-11 22:42:27.056372+08		1	1	t	f	f	f	f		f		f		一般	f	f	一般	\N	[]	[]	[]	34	
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2024-10-06 23:48:34.557827+08	1	test1	1	[{"added": {}}]	8	1
2	2024-10-06 23:54:57.541436+08	1	austin	2	[{"changed": {"fields": ["Last login", "\\u7528\\u6237\\u89d2\\u8272"]}}]	7	1
3	2024-10-08 10:11:44.684925+08	2	冷子慧	1	[{"added": {}}]	7	1
4	2024-10-08 10:15:23.717168+08	2	冷子慧	2	[]	7	1
5	2024-10-08 10:23:45.673462+08	2	冷子慧	2	[]	7	1
6	2024-10-08 14:18:19.946217+08	4	汪城波	1	[{"added": {}}]	7	1
7	2024-10-08 14:18:36.430898+08	2	冷子慧	2	[{"changed": {"fields": ["\\u7ec4\\u957f"]}}]	7	1
8	2024-10-08 14:24:46.513451+08	5	李美钰	1	[{"added": {}}]	7	1
9	2024-10-08 14:24:57.430357+08	5	李美钰	2	[{"changed": {"fields": ["\\u7ec4\\u957f"]}}]	7	1
10	2024-10-08 14:29:09.560689+08	5	李美钰	3		7	1
11	2024-10-08 14:29:39.040799+08	6	李美钰	1	[{"added": {}}]	7	1
12	2024-10-08 15:00:06.623802+08	2	冷子慧	2	[{"changed": {"fields": ["Password"]}}]	7	1
13	2024-10-08 15:06:20.96495+08	11	未知	3		8	1
14	2024-10-08 15:10:05.412891+08	7	董婷婷	1	[{"added": {}}]	7	1
15	2024-10-08 15:18:19.215791+08	7	董婷婷	3		7	1
17	2024-10-08 15:22:59.996925+08	3	austin2	3		7	1
18	2024-10-08 15:23:16.586395+08	9	陈予琳	2	[{"changed": {"fields": ["\\u7528\\u6237\\u89d2\\u8272"]}}]	7	1
19	2024-10-08 15:44:51.620691+08	10	胡夏阳	1	[{"added": {}}]	7	1
20	2024-10-08 15:45:29.18197+08	11	晴妹	1	[{"added": {}}]	7	1
21	2024-10-08 15:48:35.374184+08	9	陈予琳	2	[{"changed": {"fields": ["Password"]}}]	7	1
29	2024-10-08 17:45:05.37123+08	13	HXY胡夏阳	1	[{"added": {}}]	7	1
30	2024-10-08 17:45:35.030503+08	10	胡夏阳	3		7	1
31	2024-10-08 17:45:56.183748+08	13	HXY胡夏阳	2	[{"changed": {"fields": ["\\u7528\\u6237\\u89d2\\u8272"]}}]	7	1
32	2024-10-08 17:46:48.633704+08	11	晴妹	2	[{"changed": {"fields": ["Password", "\\u7ec4\\u957f"]}}]	7	1
33	2024-10-08 17:47:07.822742+08	13	胡夏阳	2	[{"changed": {"fields": ["Username"]}}]	7	1
34	2024-10-08 17:47:40.740549+08	14	秦嘉豪	1	[{"added": {}}]	7	1
35	2024-10-08 17:50:12.737098+08	14	秦嘉豪	2	[{"changed": {"fields": ["Password"]}}]	7	1
37	2024-10-08 17:53:12.532626+08	13	胡夏阳	2	[{"changed": {"fields": ["Password"]}}]	7	1
38	2024-10-08 17:54:18.522723+08	14	秦嘉豪	2	[{"changed": {"fields": ["Password"]}}]	7	1
40	2024-10-08 17:57:58.066732+08	17	张俊	1	[{"added": {}}]	7	1
41	2024-10-08 17:58:48.018313+08	18	魏豪	1	[{"added": {}}]	7	1
42	2024-10-08 17:59:28.45364+08	19	吴小维	1	[{"added": {}}]	7	1
43	2024-10-08 17:59:28.705133+08	9	陈予琳	2	[{"changed": {"fields": ["Last login", "\\u7528\\u6237\\u6743\\u9650"]}}]	7	1
44	2024-10-08 17:59:57.295766+08	1	super_admin	1	[{"added": {}}]	3	1
45	2024-10-08 18:00:15.996254+08	20	邓小亮	1	[{"added": {}}]	7	1
46	2024-10-08 18:00:54.925127+08	9	陈予琳	2	[{"changed": {"fields": ["\\u7528\\u6237\\u7ec4"]}}]	7	1
47	2024-10-08 18:01:12.15515+08	6	李美钰	2	[{"changed": {"fields": ["Password"]}}]	7	1
48	2024-10-08 18:01:30.772247+08	21	austin2	1	[{"added": {}}]	7	1
49	2024-10-08 18:01:42.66971+08	21	austin2	3		7	1
50	2024-10-08 18:01:58.12977+08	22	李小伟	1	[{"added": {}}]	7	1
51	2024-10-08 18:03:38.357579+08	9	陈予琳	2	[{"changed": {"fields": ["Password"]}}]	7	1
53	2024-10-08 18:04:49.891715+08	24	张凯钦	1	[{"added": {}}]	7	1
54	2024-10-08 18:05:36.986452+08	25	王微伟	1	[{"added": {}}]	7	1
55	2024-10-08 18:06:11.273061+08	26	胡小婷	1	[{"added": {}}]	7	1
56	2024-10-08 18:06:47.362692+08	27	邹敏	1	[{"added": {}}]	7	1
57	2024-10-08 18:07:27.266332+08	28	朱龙冲	1	[{"added": {}}]	7	1
58	2024-10-08 18:07:58.75384+08	2	冷子慧	2	[{"changed": {"fields": ["Password"]}}]	7	1
59	2024-10-08 18:08:02.864425+08	9	陈予琳	3		7	1
60	2024-10-08 18:08:39.265198+08	4	汪城波	2	[{"changed": {"fields": ["Password", "\\u7ec4\\u957f"]}}]	7	1
62	2024-10-08 18:40:40.289084+08	31	丁雨波	1	[{"added": {}}]	7	1
63	2024-10-09 11:15:23.15949+08	29	陈予琳	2	[{"changed": {"fields": ["Last login", "\\u7528\\u6237\\u89d2\\u8272"]}}]	7	1
64	2024-10-09 11:16:15.168447+08	29	陈予琳	2	[{"changed": {"fields": ["Password"]}}]	7	1
65	2024-10-11 11:12:21.966825+08	2	冷子慧	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
66	2024-10-11 11:12:37.711537+08	6	李美钰	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
67	2024-10-11 11:12:53.283562+08	22	李小伟	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
68	2024-10-11 11:13:05.599595+08	24	张凯钦	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
69	2024-10-11 11:13:23.441632+08	25	王微伟	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
70	2024-10-11 11:13:35.427145+08	26	胡小婷	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
71	2024-10-11 11:13:46.151212+08	27	邹敏	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
72	2024-10-11 11:13:58.943999+08	28	朱龙冲	2	[{"changed": {"fields": ["First name", "Last name"]}}]	7	1
73	2024-10-16 18:53:58.161606+08	97	未知	1	[{"added": {}}]	8	1
74	2024-10-16 19:20:58.38791+08	99	未知	1	[{"added": {}}]	8	1
75	2024-10-18 19:17:47.735427+08	32	任侠	1	[{"added": {}}]	7	1
76	2024-10-19 00:14:34.31311+08	2	冷子慧	2	[{"changed": {"fields": ["Password"]}}]	7	1
77	2024-10-21 09:16:05.120173+08	31	丁雨波	2	[{"changed": {"fields": ["\\u7ec4\\u957f"]}}]	7	1
78	2024-10-21 09:16:20.382175+08	27	邹敏	2	[]	7	1
79	2024-10-21 09:16:28.857467+08	26	胡小婷	2	[]	7	1
80	2024-10-21 09:16:40.990832+08	25	王微伟	2	[]	7	1
81	2024-10-21 09:17:08.341543+08	20	邓小亮	2	[{"changed": {"fields": ["First name", "Last name", "\\u7ec4\\u957f"]}}]	7	1
82	2024-10-21 09:17:46.771541+08	18	魏豪	2	[{"changed": {"fields": ["First name", "Last name", "\\u7ec4\\u957f"]}}]	7	1
83	2024-10-21 09:18:25.642318+08	14	秦嘉豪	2	[{"changed": {"fields": ["First name", "Last name", "\\u7ec4\\u957f"]}}]	7	1
84	2024-10-21 09:18:45.884893+08	13	胡夏阳	2	[{"changed": {"fields": ["First name", "Last name", "\\u7528\\u6237\\u89d2\\u8272", "\\u7ec4\\u957f"]}}]	7	1
85	2024-10-21 09:19:06.524164+08	11	晴妹	2	[{"changed": {"fields": ["\\u7ec4\\u957f"]}}]	7	1
86	2024-10-21 09:19:49.273303+08	8	董婷婷	2	[{"changed": {"fields": ["Last login", "\\u7528\\u6237\\u89d2\\u8272"]}}]	7	1
87	2024-10-21 09:21:29.034492+08	33	丁丽婷	1	[{"added": {}}]	7	1
88	2024-10-21 09:22:15.704739+08	34	陈怡君	1	[{"added": {}}]	7	1
89	2024-10-21 09:22:30.204122+08	14	秦嘉豪	2	[{"changed": {"fields": ["Password"]}}]	7	1
90	2024-10-21 09:44:41.468337+08	26	胡小婷	2	[{"changed": {"fields": ["Password"]}}]	7	1
91	2024-10-21 09:45:47.914542+08	27	邹敏	2	[{"changed": {"fields": ["Password"]}}]	7	1
92	2024-10-21 09:46:43.269119+08	35	金坤香	1	[{"added": {}}]	7	1
93	2024-10-21 09:48:14.431047+08	22	李小伟	2	[{"changed": {"fields": ["Password"]}}]	7	1
94	2024-10-21 09:48:33.453139+08	6	李美钰	2	[{"changed": {"fields": ["Password"]}}]	7	1
95	2024-10-21 09:48:56.344135+08	25	王微伟	2	[{"changed": {"fields": ["Password"]}}]	7	1
96	2024-10-21 09:50:02.4593+08	2	冷子慧	2	[{"changed": {"fields": ["Password"]}}]	7	1
97	2024-10-21 09:50:24.045268+08	4	汪城波	2	[{"changed": {"fields": ["Password"]}}]	7	1
98	2024-10-21 11:40:29.717128+08	36	刘永林	1	[{"added": {}}]	7	1
99	2024-10-21 11:41:41.422196+08	37	张海玲	1	[{"added": {}}]	7	1
100	2024-10-21 12:00:54.277435+08	8	董婷婷	2	[{"changed": {"fields": ["Password"]}}]	7	1
101	2024-10-21 14:11:51.356235+08	13	胡夏阳	2	[{"changed": {"fields": ["Password"]}}]	7	1
102	2024-10-21 14:12:40.858336+08	18	魏豪	2	[{"changed": {"fields": ["Password"]}}]	7	1
103	2024-10-21 14:13:07.383435+08	11	晴妹	2	[{"changed": {"fields": ["Password"]}}]	7	1
104	2024-10-21 14:13:36.809328+08	20	邓小亮	2	[{"changed": {"fields": ["Password"]}}]	7	1
105	2024-10-21 14:14:13.324453+08	33	丁丽婷	2	[{"changed": {"fields": ["Password"]}}]	7	1
106	2024-10-21 14:17:25.910457+08	31	丁雨波	2	[{"changed": {"fields": ["Password"]}}]	7	1
107	2024-10-21 14:18:27.327082+08	31	丁雨波	2	[]	7	1
108	2024-11-01 19:11:59.302191+08	2	冷子慧	2	[{"changed": {"fields": ["Password"]}}]	7	1
109	2024-11-08 22:55:32.45725+08	4	汪城波	2	[{"changed": {"fields": ["Password"]}}]	7	1
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-10-06 16:14:58.716164+08
2	auth	0001_initial	2024-10-06 16:14:58.816124+08
3	admin	0001_initial	2024-10-06 16:14:58.84641+08
4	admin	0002_logentry_remove_auto_add	2024-10-06 16:14:58.857198+08
5	admin	0003_logentry_add_action_flag_choices	2024-10-06 16:14:58.867225+08
6	contenttypes	0002_remove_content_type_name	2024-10-06 16:14:58.921214+08
7	auth	0002_alter_permission_name_max_length	2024-10-06 16:14:58.931842+08
8	auth	0003_alter_user_email_max_length	2024-10-06 16:14:58.942785+08
9	auth	0004_alter_user_username_opts	2024-10-06 16:14:58.951859+08
10	auth	0005_alter_user_last_login_null	2024-10-06 16:14:58.965672+08
11	auth	0006_require_contenttypes_0002	2024-10-06 16:14:58.968656+08
12	auth	0007_alter_validators_add_error_messages	2024-10-06 16:14:58.978781+08
13	auth	0008_alter_user_username_max_length	2024-10-06 16:14:58.994647+08
14	auth	0009_alter_user_last_name_max_length	2024-10-06 16:14:59.005775+08
15	auth	0010_alter_group_name_max_length	2024-10-06 16:14:59.022427+08
16	auth	0011_update_proxy_permissions	2024-10-06 16:14:59.032126+08
17	auth	0012_alter_user_first_name_max_length	2024-10-06 16:14:59.043229+08
18	sessions	0001_initial	2024-10-06 16:14:59.062027+08
19	sales	0001_initial	2024-10-06 18:11:45.067148+08
20	customers	0001_initial	2024-10-06 23:26:21.764361+08
21	customers	0002_customer_is_contacted_customer_is_wechat_added	2024-10-13 17:35:59.557249+08
22	customers	0003_customer_additional_students_customer_comments_count_and_more	2024-10-16 11:56:32.322483+08
23	customers	0004_alter_customer_additional_students_and_more	2024-10-16 13:56:09.311495+08
24	customers	0005_customer_cloud_computing_promotion_content_and_more	2024-10-16 14:29:04.965866+08
25	customers	0006_remove_customer_student_batch_and_more	2024-10-16 18:49:35.317188+08
26	customers	0007_alter_customer_cloud_computing_promotion_content_and_more	2024-10-16 18:53:12.609983+08
27	customers	0008_alter_customer_name	2024-10-16 19:20:10.135025+08
28	customers	0009_customer_student_batch	2024-10-18 12:55:57.766256+08
29	token_blacklist	0001_initial	2024-10-22 11:59:54.637602+08
30	token_blacklist	0002_outstandingtoken_jti_hex	2024-10-22 11:59:54.655554+08
31	token_blacklist	0003_auto_20171017_2007	2024-10-22 11:59:54.692227+08
32	token_blacklist	0004_auto_20171017_2013	2024-10-22 11:59:54.737385+08
33	token_blacklist	0005_remove_outstandingtoken_jti	2024-10-22 11:59:54.781234+08
34	token_blacklist	0006_auto_20171017_2113	2024-10-22 11:59:54.809425+08
35	token_blacklist	0007_auto_20171017_2214	2024-10-22 11:59:54.875339+08
36	token_blacklist	0008_migrate_to_bigautofield	2024-10-22 11:59:54.956805+08
37	token_blacklist	0010_fix_migrate_to_bigautofield	2024-10-22 11:59:54.997079+08
38	token_blacklist	0011_linearizes_history	2024-10-22 11:59:54.999926+08
39	token_blacklist	0012_alter_outstandingtoken_user	2024-10-22 11:59:55.014752+08
40	customers	0010_customer_supervisor_comments	2024-11-02 09:18:41.351612+08
41	customers	0011_alter_customer_student_batch	2024-11-10 10:09:58.393578+08
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
1upjncp0me9x8ohd6teym87wrd8y1ukb	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sxPFx:lNfnn6sA2mYYyaP724vqOpwNYrUKlSxY6QLkqLCiNms	2024-10-20 19:16:57.700267+08
dfxlq1wzhd4dsjqr417waich1zhzjnq8	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sxkEA:2Ia3_1F_ehX-F-vXjlWq0cnhOUPMSdrqCJ3n-FNP-0w	2024-10-21 17:40:30.301779+08
xlj14h2p2ry66jvnui2a5swysm6r69ob	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sxoqs:X8tXTxAVorEuDvg6__hEjNDWet1jS8k0g-TPLxVfzGs	2024-10-21 22:36:46.96012+08
kmya7y9bt5wmlydei41kndcqewom2ldm	.eJxVjEEOwiAQRe_C2hAoFDsu3fcMzQzMSNVAUtqV8e7apAvd_vfef6kJtzVPW-NlmpO6qE6dfjfC-OCyg3THcqs61rIuM-ld0QdteqyJn9fD_TvI2PK3BuvMWbgT24OL0dBgHBsSsCggBiAQoBdMgY0PicSxoITgKHI_eFDvD-4bOKM:1t9Qca:Vn8QCqRvbNoRDPMK5OgGHoua4R0bsYVJnHgv-6swrec	2024-11-22 23:10:00.17832+08
fd9kwdmdpd6ak2b9j5spwdbq7apoayxs	.eJxVjDEOwjAMRe-SGUWO3DoJIztnqGLHJQWUSk07Ie4OlTrA-t97_2WGtK1l2Jouw5TN2QRz-t04yUPrDvI91dtsZa7rMrHdFXvQZq9z1uflcP8OSmrlW0ccMY4q7AmEmCQBc-iy6xSRgJwnjKQSsRsxueABoQfOLqBXkN68P-PsN0Q:1sy4WX:_T4VcUkMEsUx953uHI7D_Dx3UFf4reb4hhqrAhkYvmw	2024-10-22 15:20:49.599423+08
7va0mqe1ckofa2f88451gjlnnfc7xg8i	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sy4x4:YRaEDOf0xtklgGzjh3xAgscYE182UEkYhjqwdVX1alQ	2024-10-22 15:48:14.812199+08
y88xoureus4vr9td3z06c75hi2f35q37	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sy4x4:YRaEDOf0xtklgGzjh3xAgscYE182UEkYhjqwdVX1alQ	2024-10-22 15:48:14.828276+08
mdvm8758cygagzeoweeufnw70ssb9zz9	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sy6kR:vkCGV2zQApcNtBGC87Dpz7LMPU-H4nZW3HuCMorbCk0	2024-10-22 17:43:19.834456+08
zebon0a193pcueyw48soczqfoib3uoda	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1tA80d:JLXOfBFP1eKkwBlDBr5JERVieygo1UJS8HOeDPghOus	2024-11-24 21:29:43.469237+08
q6z62k8mmjx3639ggaxxfg0z0zv8zzip	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1tA95Y:THfzIKflbKm0jC5qo5gVp2yJdi7Ktjzz837PJc8YQdA	2024-11-24 22:38:52.392848+08
4y3jnihfulxfwk4c41s3rqi7rz7mxjqx	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1tAUi1:Z181lwDtZmHUPcVlMNoUuXwwVJmvw-4sNZbFhAmsC3I	2024-11-25 21:44:01.167248+08
mt2pqzyxjsjjhc2rr0z02q40rflcpvdq	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sy7dM:mOiRJ3Xa36q1sTLdJcp5IiZN-TrEStZeSlU4YuntJqU	2024-10-22 18:40:04.292209+08
c1c58h1lsom0w4p4azeykxl8egxg6f7x	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1syS8W:yPLyS3dFC-d3XTnwAv84lcC4Ydxci99AyuLg6YEgzR0	2024-10-23 16:33:36.085126+08
1v98n9wls6a54qipkxqfauecbsr31bey	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1sz643:g5jq3NJ3PPSPceyazUJDeOKU3VWXSm4EEXCDPHnRvzc	2024-10-25 11:11:39.971193+08
f3d2bbxylnv068bjiiv2h65gwtfd4ldr	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1t2h0l:fM9kk72LtowYRyyz3pyKeQytRwwNEsmTy3slTiB6NeI	2024-11-04 09:15:07.743452+08
8do8umehqkwxukl35m5335q6a2jkdjhl	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1tArfa:f27mB-AWTXQZvDUCY7c1mroJ93tVXEPo2jwMPFB-3Zk	2024-11-26 22:15:02.213068+08
qwu5aejw8a3ykqwt0hprkbvmhxr9dswy	.eJxVjMsOwiAQRf-FtSG8YVy67zeQgUGpGkhKuzL-uzbpQrf3nHNfLOK21riNssSZ2JlJdvrdEuZHaTugO7Zb57m3dZkT3xV-0MGnTuV5Ody_g4qjfmunTVJIQloIGAJcyQklXNBAOZAQ3uikrHGWdLbggaQCLxAx5AIpK_b-ALk8Nxs:1tB7lD:_02VC2nLjkvlpg7XwcDhOAJkPVqswoDkwBjb0Q_kLLE	2024-11-27 15:25:55.0519+08
7fymlmu9ie9xbdw5ts2y726b7myy456u	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1t73mv:IeskufcHWI-sHqjDnzF6dzq_aXiKFeyBgqRqAsARMHs	2024-11-16 10:22:53.165125+08
g5fs9qc26x6tmy5tdeyerydgwmf2118d	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1t73t8:AJZ_7RDZJyeBFvVaXcoEGUMYS7sh02-6KvZ0AZW_i_Y	2024-11-16 10:29:18.208324+08
2fc9b4fndvp6496veryfmksvk5jzvb2t	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1t74rQ:F653jrFd6GEp0heme3RKaDn50_lPrjpuzwExGgRAtiA	2024-11-16 11:31:36.108173+08
2qdfqfsba4lnu82uzz3qdrxk7dcci8tn	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1t7BV4:d_Cfg8vIRbazYtMvwEL5ySiY99MQ9UpXGtmFajZ8Guw	2024-11-16 18:36:58.393686+08
wrx36z3hja1zh928mfgpluzvenwxwssb	.eJxVjDsOwjAQBe_iGln-sFkvJX3OYPmzxgHkSHFSIe4OkVJA-2bmvYQP21r91nnxUxYXocXpd4shPbjtIN9Du80yzW1dpih3RR60y3HO_Lwe7t9BDb1-a6ctDaDOSAwDabRQwBagothGMkapENE4SGyVKUQOIzpgIlPAYMji_QGf0zZ-:1t9MHW:-szThode3tNucYfnGB_2nKnF2Zek2gQFpkJ5UUdpmtg	2024-11-22 18:31:58.839449+08
\.


--
-- Data for Name: sales_salesuser_groups; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.sales_salesuser_groups (id, salesuser_id, group_id) FROM stdin;
\.


--
-- Data for Name: sales_salesuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.sales_salesuser_user_permissions (id, salesuser_id, permission_id) FROM stdin;
\.


--
-- Data for Name: token_blacklist_outstandingtoken; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.token_blacklist_outstandingtoken (id, token, created_at, expires_at, user_id, jti) FROM stdin;
1	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzU3MDkxMywiaWF0IjoxNzI5NTcwOTEzLCJqdGkiOiI4ZGViY2MwZDkxZjQ0ODc4OTBlNmM0NGNkYTUyY2Q1MCIsInVzZXJfaWQiOjF9.JEyNMdrGlBBqpjAmHMpJG7VOLOENwnVHSQx27JwWZyA	2024-10-22 12:21:53.039898+08	2052-03-09 12:21:53+08	1	8debcc0d91f4487890e6c44cda52cd50
2	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzU3OTcwNywiaWF0IjoxNzI5NTc5NzA3LCJqdGkiOiJjNDQ3ZjMzNWU0YjQ0ZjhjYjUyYzQzMjgwYzM2N2NiNSIsInVzZXJfaWQiOjF9.1snpBXPSK5xCLmgeXmrSCxmuZhxsQNSJtpFjaJSvm2Y	2024-10-22 14:48:27.805153+08	2052-03-09 14:48:27+08	1	c447f335e4b44f8cb52c43280c367cb5
3	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzU5NDAzMywiaWF0IjoxNzI5NTk0MDMzLCJqdGkiOiJiMTY3Zjc0ODU0YTY0MTk5YWU4NmE2YWY1MzYzNjgwNSIsInVzZXJfaWQiOjM0fQ.UsNa9pilPL_i13zQgPhBRsVKUjSOTzT-XsbLiMod2rs	2024-10-22 18:47:13.790211+08	2052-03-09 18:47:13+08	34	b167f74854a64199ae86a6af53636805
4	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzY0ODMxMCwiaWF0IjoxNzI5NjQ4MzEwLCJqdGkiOiIxYzYzZDk5NTlhNzg0ZDRkYjcwMzNjYzRiYzAyYzc5MCIsInVzZXJfaWQiOjF9.w-UIBR5ILlIKszVLHOd5Gv--hX5wUdgRDihD5YgJLnU	2024-10-23 09:51:50.468233+08	2052-03-10 09:51:50+08	1	1c63d9959a784d4db7033cc4bc02c790
5	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzY1MjUwMCwiaWF0IjoxNzI5NjUyNTAwLCJqdGkiOiJhOWEyZDJmNzQwYzM0MjBmOWJkZDE5YWQwNTBjNGYyMCIsInVzZXJfaWQiOjF9.WbufwZNDVbNfnbhANXCS6-W316j1q0vKlNNAbkqCcTc	2024-10-23 11:01:40.152674+08	2052-03-10 11:01:40+08	1	a9a2d2f740c3420f9bdd19ad050c4f20
6	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzY1MzQwNSwiaWF0IjoxNzI5NjUzNDA1LCJqdGkiOiI5M2FmYWFmYTcyNmQ0OGQ3OWM0ZTJlNmMxZmUxYTU4MSIsInVzZXJfaWQiOjF9.VYAKqU4yd_ZJDbVazo-HwbabLNnHTnt_ijnU579Hj5U	2024-10-23 11:16:45.332071+08	2052-03-10 11:16:45+08	1	93afaafa726d48d79c4e2e6c1fe1a581
7	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzY5NDU3OCwiaWF0IjoxNzI5Njk0NTc4LCJqdGkiOiI3N2UxMDcxNzQzNmM0N2NkYjJmNDA0NWM2OTE2OTY4MSIsInVzZXJfaWQiOjF9.RKXpVcP2i6CeePQBPVxv6z2vpUNjxo34crGnMn-KgXY	2024-10-23 22:42:58.99445+08	2052-03-10 22:42:58+08	1	77e10717436c47cdb2f4045c69169681
8	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzY5NTExNSwiaWF0IjoxNzI5Njk1MTE1LCJqdGkiOiJmNmM4NWQ3NWIyOWY0YTczOGQ4ZTJhYmExOTAzNDk2MSIsInVzZXJfaWQiOjF9.bG62x1PYPNeX5ztZWVHlGxfUrIuxXhZC7Y6RqJqXqC4	2024-10-23 22:51:55.04115+08	2052-03-10 22:51:55+08	1	f6c85d75b29f4a738d8e2aba19034961
9	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5MzY5NjI0OSwiaWF0IjoxNzI5Njk2MjQ5LCJqdGkiOiIxOTU2MzcwYmMxYmQ0OTM2OWY2ZWJiODc1ODMxMDVkOCIsInVzZXJfaWQiOjF9.r711YFU_-rbuIy9Run_MJuloZHwMiTSBk4oOByP6J5I	2024-10-23 23:10:49.753851+08	2052-03-10 23:10:49+08	1	1956370bc1bd49369f6ebb87583105d8
10	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5NDQzNjg0MiwiaWF0IjoxNzMwNDM2ODQyLCJqdGkiOiJmZmRkNDVjY2YyYjc0Y2JlYmYwZGE0ODg2NzFkODA4NyIsInVzZXJfaWQiOjF9.D7EJocHu7ejFhtccfoUJHUIfdxAQiIkWxxDMX9L4wxI	2024-11-01 12:54:02.368325+08	2052-03-19 12:54:02+08	1	ffdd45ccf2b74cbebf0da488671d8087
11	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5NDQ0NjE4MiwiaWF0IjoxNzMwNDQ2MTgyLCJqdGkiOiI2YjAwMTI0NjNhYzE0MThlOGQ3NDY0ZTE4NTg2OTZiNyIsInVzZXJfaWQiOjF9.p8MXAJm0vqCQ1gAlBsOCOnFEJOsTAYPRVIYka1fambQ	2024-11-01 15:29:42.505745+08	2052-03-19 15:29:42+08	1	6b0012463ac1418e8d7464e1858696b7
12	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MjU5NDQ0NjI3OCwiaWF0IjoxNzMwNDQ2Mjc4LCJqdGkiOiI4NjY2MzMwYmExYjA0ZTkzOGExMDlkNzQ3ODlhOTI4NSIsInVzZXJfaWQiOjF9.fsm93R557lAA-Kl5GDbHDnORP4ricB4dgnFh5nwGDSQ	2024-11-01 15:31:18.752588+08	2052-03-19 15:31:18+08	1	8666330ba1b04e938a109d74789a9285
\.


--
-- Data for Name: token_blacklist_blacklistedtoken; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.token_blacklist_blacklistedtoken (id, blacklisted_at, token_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 32, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: customers_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.customers_customer_id_seq', 434, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 109, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 41, true);


--
-- Name: sales_salesuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.sales_salesuser_groups_id_seq', 2, true);


--
-- Name: sales_salesuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.sales_salesuser_id_seq', 37, true);


--
-- Name: sales_salesuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.sales_salesuser_user_permissions_id_seq', 1, true);


--
-- Name: token_blacklist_blacklistedtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.token_blacklist_blacklistedtoken_id_seq', 1, false);


--
-- Name: token_blacklist_outstandingtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.token_blacklist_outstandingtoken_id_seq', 12, true);


--
-- PostgreSQL database dump complete
--

