def longestTextReceivedQuery(): 
    return """
        select text, length(text) as chars
        from message m
        where
        text not like '%https%'
        and
        text not like 'Liked%'
        and
            datetime (m.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime")  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime")  < '2023-01-01'
        and
            is_from_me=0
        and
            text is not null
        order by chars desc
        limit 5;
    """
def longestTextSentQuery():
    return """
        select text, length(text) as chars
        from message m
        where
        text not like '%https%'
        and
        text not like 'Liked%'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=1
        and
            text is not null
        order by chars desc
        limit 5;
    """

def mostSentText2():
    return """
        SELECT text, count(*) as cnt
        FROM message m
        WHERE
            text is not null
        and
            is_from_me=1
        and
            text REGEXP '[abcdefghijklmnopABCDEFGHIJKLMNOP]'
        and
            LENGTH(text)>2
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        GROUP by text
        ORDER BY cnt desc
        limit 5;
    """
def mostSentText5():
    return """
        SELECT text, count(*) as cnt
        FROM message m
        WHERE
            text is not null
        and
            is_from_me=1
        and
            text REGEXP '[abcdefghijklmnopABCDEFGHIJKLMNOP]'
        and
            LENGTH(text)>5
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        GROUP by text
        ORDER BY cnt desc
        limit 5;
    """


def mostTalkedToQuery(): 
    return """
        select h.id,count(1) as cnt,round(
        sum(case when m.is_from_me then 1 else 0 end) * 1.0 / count(1) * 100.0,2)
        from message m join handle h on h.rowid = m.handle_id
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch','localtime') >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') < '2023-01-01'
        and
            text is not null
        group by h.id
        order by cnt desc
        limit 10;
    """
def textReceivedNightQuery(): 
    return """
        select h.id, count(*) as cnt
        from message m join handle h on h.rowid = m.handle_id
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=0
        and
            text is not null
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') >='00'
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') <='03'
        group by h.id
        order by cnt desc
        limit 5;
    """
def textReceivedByTimeQuery(): 
    return """
        select strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') as time, count(*) as cnt
        from message m
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=0
        and
            text is not null
        group by time
        order by cnt desc
        limit 5;
    """

def textSentByTimeQuery(): 
    return """
        select strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') as time, count(*) as cnt
        from message m
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=1
        and
            text is not null
        group by time
        order by cnt desc
        limit 5;
    """
def textSentNightQuery(): 
    return """
        select h.id, count(*) as cnt
        from message m join handle h on h.rowid = m.handle_id
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=1
        and
            text is not null
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') >='00'
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') <='03'
        group by h.id
        order by cnt desc
        limit 10;
    """

def totalCharsReceivedQuery(): 
    return """
        select sum(length(text)) as Total_Chars_Received
        from message m
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=0
        and
            text is not null;
    """
def totalCharsSentQuery(): 
    return """
        select sum(length(text)) as Total_Chars_Sent 
        from message m 
        where 
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01' 
        and 
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01' 
        and 
            is_from_me=1 
        and 
            text is not null;"""
def totalTextReceivedQuery(): 
    return """
        select count(text) as Total_Texts_Received
        from message m
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=0
        and
            text is not null;
    """
def totalTextSentQuery(): 
    return """
        select count(text) as Total_Texts_Sent
        from message m
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=1
        and
            text is not null;
    """
            
def textSentMorningQuery(): 
    return """
        select h.id, count(*) as cnt
        from message m join handle h on h.rowid = m.handle_id
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=1
        and
            text is not null
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') >='06'
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') <='09'
        group by h.id
        order by cnt desc
        limit 5;
    """
def textReceivedMorningQuery(): 
    return """
        select h.id, count(*) as cnt
        from message m join handle h on h.rowid = m.handle_id
        where
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  >= '2022-01-01'
        and
            datetime (m.date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime')  < '2023-01-01'
        and
            is_from_me=0
        and
            text is not null
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') >='06'
        and
            strftime('%H',date / 1000000000 + strftime ('%s', '2001-01-01'), 'unixepoch', 'localtime') <='09'
        group by h.id
        order by cnt desc
        limit 5;
    """