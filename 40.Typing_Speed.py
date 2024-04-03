from tkinter import *
from PIL import Image
import PIL.ImageTk as ImageTk
import time
from tkinter import font
import random

root = Tk()
root.title("Typing Speed Test")
root.geometry("500x500+100+40")

words = ['a', 'ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'act', 'action', 'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'age', 'agency', 'agent', 'ago', 'agree', 'agreement', 'ahead', 'air', 'all', 'allow', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'American', 'among', 'amount','anasticia','vishnu','brahma','shiv','dieting','keenly',
'analysis', 'and', 'animal', 'another', 'answer', 'any', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area', 'argue', 'arm', 'around', 'arrive', 'art', 'article', 'artist', 'as', 'ask','aspirin','demon','bioinformatics','aslike','stibnite','chersonese','grommet','nauseant','athena','zeus','quilling','dinoysus','demeter','aphrodite','ares','hades','poseidon','hera','hestia','apollo','hermes','hephaestus', 'assume', 'attack', 'attention', 'attorney', 'audience', 'author', 'authority', 'available', 'avoidaway', 'baby', 'back', 'bad', 'bag', 'ball', 'bank', 'bar', 'base', 'be', 'beat', 'beautiful', 'because', 'become', 'bed', 'before', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'big', 'bill', 'billion', 'bit', 'black', 'blood', 'blue', 'board', 'body', 'book', 'born', 'both', 'boxboy', 'break', 'bring', 'brother', 'budget', 'build', 'building', 'business', 'but', 'buy', 'by', 'call', 'camera', 'campaign', 'can', 'cancer', 'candidate', 'capital', 'car', 'card', 'care', 'career', 'carry', 'case', 'catch', 'cause', 'cell', 'center', 'central', 'century', 'certain', 'certainly', 'chair', 'challenge', 'chance', 'change', 'character', 'charge', 'check', 'child', 'choice', 'choose', 'church', 'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly', 'close', 'coach', 'cold', 'collection', 'college', 'color', 'come', 'commercial', 'common', 'community', 'company', 'compare', 'computer', 'concern', 'condition', 'conference', 'Congress', 'consider', 'consumer', 'contain', 'continue', 'control', 'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create', 'crime', 'cultural', 'culture', 'cup', 'current', 'customer', 'cut', 'dark', 'data', 'daughter', 'day', 'dead', 'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'Democrat', 'democratic', 'describe', 'design', 'despite', 'detail', 'determine', 'develop', 'development', 'die', 'difference', 'different',
'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion', 'disease', 'do', 'doctor', 'dog', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during', 'each', 'early', 'east', 'easy', 'eat', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight', 'either', 'election', 'else', 'employee', 'end', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment', 'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody', 'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience', 'expert', 'explain', 'eye', 'face', 'fact', 'factor', 'fail', 'fall', 'family', 'far', 'fast', 'father', 'fear', 'federal', 'feel', 'feeling', 'few', 'field', 'fight', 'figure', 'fill', 'film', 'final', 'finally', 'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five', 'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front', 'full', 'fund', 'future', 'game', 'garden', 'gas', 'general', 'generation', 'get', 'girl', 'give', 'glass', 'go', 'goal', 'good', 'government', 'great', 'green', 'ground', 'group', 'grow', 'growth', 'guess', 'gun', 'guy', 'hair', 'half', 'hand', 'hang', 'happen', 'happy', 'hard', 'have', 'he', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'her', 'here', 'herself', 'high', 'him', 'himself', 'his', 'history', 'hit', 'hold', 'home', 'hope', 'hospital', 'hot', 'hotel', 'hour', 'house', 'how', 'however', 'huge', 'human', 'hundred', 'husband', 'idea', 'identify', 'if', 'image', 'imagine', 'impact', 'important', 'improve', 'in', 'include', 'including', 'increase', 'indeed', 'indicate', 'individual', 'industry', 'information', 'inside', 'instead', 'institution', 'interest', 'interesting', 'international', 'interview', 'into', 'investment', 'involve', 'issue', 'it', 'item', 'its', 'itself', 'job', 'join', 'just', 'keep', 'key', 'kid', 'kill', 'kind', 'kitchen', 'know', 'knowledge', 'land', 'language', 'large', 'last', 'late', 'later', 'laugh', 'law', 'lawyer', 'lay', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'leg', 'legal', 'less', 'let', 'letter', 'level', 'lie', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen', 'little', 'live', 'local', 'long', 'look', 'lose', 'loss', 'lot', 'love', 'low', 'machine', 'magazine', 'main', 'maintain', 'major', 'majority', 'make', 'man', 'manage', 'management', 'manager', 'many', 'market', 'marriage', 'material', 'matter', 'may', 'maybe', 'me', 'mean', 'measure', 'media', 'medical', 'meet', 'meeting', 'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million', 'mind', 'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most', 'mother', 'mouth', 'move', 'movement', 'movie', 'mr', 'mrs', 'much', 'music', 'must', 'my', 'myself', 'name', 'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network', 'never', 'new', 'news', 'newspaper', 'next', 'nice', 'night', 'no', 'none', 'nor', 'north', 'not', 'note', 'nothing', 'notice', 'now', "n't", 'number', 'occur', 'of', 'off', 'offer', 'office', 'officer', 'official', 'often', 'oh', 'oil', 'ok', 'old', 'on', 'once', 'one', 'only', 'onto', 'open', 'operation', 'opportunity', 'option', 'or', 'order', 'organization', 'other', 'others', 'our', 'out', 'outside', 'over', 'own', 'owner', 'page', 'pain', 'painting', 'paper', 'parent', 'part', 'participant', 'particular', 'particularly', 'partner', 'party', 'pass', 'past', 'patient', 'pattern', 'pay', 'peace', 'people', 'per', 'perform', 'performance', 'perhaps', 'period', 'person', 'personal', 'phone', 'physical', 'pick', 'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'PM', 'point', 'police', 'policy', 'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'power', 'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price', 'private', 'probably', 'problem', 'process', 'roduce', 'product', 'production', 'professional', 'professor', 'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push', 'put', 'quality', 'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate', 'rather', 'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent', 'recently', 'recognize', 'record', 'red', 'reduce', 'reflect', 'region', 'relate', 'relationship', 'religious', 'remain', 'remember', 'remove', 'report', 'represent', 'Republican', 'require', 'research', 'resource', 'respond', 'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right', 'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'run', 'safe', 'same', 'save', 'say', 'scene', 'school', 'science', 'scientist', 'score', 'sea', 'season', 'seat', 'second', 'section', 'security', 'see', 'seek', 'seem', 'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'set', 'seven', 'several', 'sex', 'sexual', 'shake', 'share', 'she', 'shoot', 'short', 'shot', 'should', 'shoulder', 'show', 'side', 'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister', 'sit', 'site', 'situation', 'six', 'size', 'skill', 'skin', 'small', 'smile', 'so', 'social', 'society', 'soldier', 'some', 'somebody', 'someone', 'something', 'sometimes', 'son', 'song', 'soon', 'sort', 'sound', 'source', 'south', 'southern', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport', 'spring', 'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay', 'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure', 'student', 'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly', 'suffer', 'suggest', 'summer', 'support', 'sure', 'surface', 'system', 'table', 'take', 'talk', 'task', 'tax', 'teach', 'teacher', 'team', 'technology', 'television', 'tell', 'ten', 'tend', 'term', 'test', 'than', 'thank', 'that', 'the', 'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three', 'through', 'throughout',
'throw', 'thus', 'time', 'to', 'today', 'together', 'tonight', 'too', 'top', 'total', 'tough', 'toward', 'town', 'trade', 'traditional', 'training', 'travel', 'treat', 'treatment', 'tree', 'trial', 'trip', 'trouble', 'true', 'truth', 'try', 'turn', 'TV', 'two', 'type', 'under', 'understand', 'unit', 'until', 'up', 'upon', 'ususe', 'usually', 'value', 'various', 'very', 'victim', 'view', 'violence', 'visit', 'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'war', 'watch', 'water', 'way', 'we', 'weapon', 'wear', 'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where', 'whether', 'which', 'while', 'white', 'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'will', 'win', 'wind', 'window', 'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world',
'worry', 'would','for','in','to','opt','set','into','at', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your','yourself']

seq,left,cl,key,loc,wrong,prev,tim,spd,err,seq1,total,cha = "",'                             ',0,'',0,'',[],60,0,0,[],200,False

def para(e=None):
    global cha,main_frame,main_frame2
    if cha == False:
        cha = True
        main_frame.forget()
        main_frame2.pack(fill=BOTH,expand=1)

def result(e=None):
    global tim,spd,err,text1,text2,text3
    up = Toplevel(main_frame)
    up.geometry("350x130+150+100")
    label = Label(up,text="CONGRATULATIONS!!",fg="dark green",font=("Times New Roman",19))
    label.pack(pady=10,ipadx=3)
    a = "You have successfully complete the typing speed test\nwith the speed of "+str(canvas.itemcget(text2,'text'))+" wpm and with accuracy of "+ str(canvas.itemcget(text3,'text'))+ "%"
    label2 = Label(up,text=a,fg="green",font=("Times New Roman",12))
    label2.pack(pady=10,ipadx=1)

def change(e=None):
    global tim,spd,err,canvas,text1,text2,text3,box1,box2,total,seq,seq1,left,cl,loc,wrong,prev,key,cha,main_frame,main_frame2
    if cha:
        main_frame.pack(fill=BOTH,expand=1)
        main_frame2.forget()
    if e == 1:
        tim = 60
        total = 200
        canvas.itemconfig(text1,text=tim)
    elif e == 2:
        tim = 120
        total = 450
        canvas.itemconfig(text1,text=tim)
    elif e == 3:
        tim = 300
        total = 830
        canvas.itemconfig(text1,text=tim)
    box1.delete("1.0",END)
    box2.delete("1.0",END)
    seq,left,cl,loc,wrong,prev,spd,err,seq1,key = "",'                             ',0,0,'',[],0,0,[],''
    canvas.itemconfig(text2,text=spd)
    canvas.itemconfig(text3,text="100")
    root.bind("<Key>",type)
    insert()

def error(e=None):
    global wrong,prev,canvas,text1,text2,text3,err,seq1
    if wrong:
        a = len(seq1)
        err += 1
        s = ((a-err)/a)*100
        s = int(s*100)/100
        canvas.itemconfig(text3,text=str(s))

def speed(e=None):
    global canvas,text1,text2,text3,key,tim,prev,seq,left,wrong,spd
    if wrong == '':
        spd += 1
        if total == 200:
            canvas.itemconfig(text2,text=str(spd))
        elif total == 450:
            canvas.itemconfig(text2,text=str(round(spd/2)))
        elif total == 823:
            if round(spd/5) == 0:
                canvas.itemconfig(text2,text=str(1))
            else:
                canvas.itemconfig(text2,text=str(round(spd/5)))

def selection(e=None):
    global box1,box2,words,seq,left,key,prev
    if len(left) > 29:
        a = box1.get("1.0",END)
        b = -(a[::-1].find(" ")+1) + len(a)
        q = a[:b]
        d = q[q.find(" ")+1:]
        y = len(q) - len(d)
        d = " " + d
        p = -(d[::-1].find(" ")+1) + len(d)
        s = "1."+str(b+1)   
        e = "1."+ str(len(a[b+1:])+b+1)
        if b != len(a):
            if key != 'space':
                if wrong:
                    box1.tag_remove("Green",s,e)
                    box1.tag_add("Red",s,e)
                    box1.tag_add("Strike",s,e)
                else:
                    box1.tag_remove("Red","1.0",END)
                    box1.tag_remove("Strike",s,e)
                    box1.tag_add("Green",s,e)
            else:
                box1.tag_remove("Red","1.0",END)
                box1.tag_remove("Green","1.00",END)
            if len(prev) >= 1:
                l = 1
                if len(prev) == 1:  i = 0
                else:   i = -1
                while d != "" and len(prev)>=l:
                    if prev[i] != d[p+1:]:
                        s = "1."+str(p+y)
                        e = "1."+str(len(d[p+1:])+p+y)
                        box1.tag_add("Strike",s,e)
                    d = d[:p]
                    p = -(d[::-1].find(" ")+1) + len(d)
                    if p == len(d) or d.isspace():
                        d = ""
                    i -= 1
                    l += 1
            if a[0] != ' ':
                p = -(d[::-1].find(" ")+1) + len(d)
                u,v = 0,0
                u = a.count(' ')
                v = a.find(' ')
                t = left[:-(len(a)-1)]
                if t == '' or t.isspace():
                    g = 29
                else:
                    g = -((t[::-1]).find(' ')) + len(t) 
                h = left[g:].find(' ') + len(left[:g])
                j = left[g:h]
                if j != prev[-u]:
                    box1.tag_add("Strike","1.0","1."+str(v))
        else:
            box1.tag_add("Red","1.0",END)
            box1.tag_add("Strike","1.0",END)

def times(e=None):
    global text1,text2,text3,canvas,box1,box2,prev,tim
    if key:
        tim -= 1
        canvas.itemconfig(text1,text=str(tim+1))
        if tim == 0:
            canvas.itemconfig(text1,text="0")
            root.unbind("<Key>")
            box1.tag_remove("Red","1.0",END) 
            result()
        else:
            label.after(1000,times)

def space(e=None):
    global words,seq,left,wrong,loc,box1,box2,prev
    if wrong:
        if left[-2]!=" ":
            a = seq.index(" ")
            prev.append(seq[:a])
            seq = seq[loc:]
            a = seq.index(" ")
            box2.delete("1.0","1."+str(a+1))
            seq = seq[a+1:]
        else:
            left = left[:-1]
            wrong = ""
    else:
        prev.append(seq[:loc-1])
        seq = seq[loc:]
    speed()
    error()
    wrong = ""
    loc=0

def insert():
    global canvas,box2,words,seq,total
    p = list.copy(words)
    t = len(p)
    for i in range (total,0,-1):
        a = random.randint(0,t-1)
        b = p[a]
        t -= 1
        p.remove(b)
        box2.insert(END,(b+" "))
        seq += b+" "
        seq1.append(b)

def type(e):
    global box1,box2,seq,canvas,left,cl,label,key,loc,wrong,tim
    e = str(e)
    key = e[e.find('keysym')+7]
    if e[e.find('keysym')+8]=='p':
        key = 'space'
    elif e[e.find('keysym')+8]=='e':
        key = 'return'
    elif e[e.find('keysym')+8]=='a':
        key = 'back'
    if tim == 60 or tim==120 or tim == 300:
        times()
    if key != 'back':
        if key == seq[loc] or (key == "space" and seq[loc]==" "):
            loc += 1
            box2.delete("1.0","1.01") 
            if key != 'space' and key!='return':
                left += key
            elif key == 'space':
                left += ' '
                space()
            elif key == 'return':
                left += "_"
            cl = cl + 1.8
            cl = round(int(cl*100)/10)/10
            f = 28-cl
            f = int(round(f))
            box1.delete("1.0",END)
            if f<0:
                box1.insert("1.0",left[-16:])
            else:
                box1.insert("1.0",left[:f-1]+left[29:])
        else:
            if key != 'A' and key!='C' and key!="S" and key!="R" and key!="D":
                cl = cl + 1.8
                cl = round(int(cl*100)/10)/10
                f = 28-cl
                f = int(round(f))
                box1.delete("1.0",END)
                if key == 'space':   
                    left += ' '
                    wrong += ' '
                    space()
                elif key == 'return':   
                    left += "_"
                    wrong += '_'
                elif key != 'space' and key!='return':  
                    left += key
                    wrong += key
                if f<0:
                    box1.insert("1.0",left[-16:])
                else:
                    box1.insert("1.0",left[:f-1]+left[29:])
    if key == 'back':
        if (wrong or loc>=1) and len(left)>29:
            cl = cl - 1.8
            cl = round(int(cl*100)/10)/10
            f = 28-cl
            f = int(round(f))
            if wrong == '':
                loc -= 1
                box2.insert("1.0",seq[loc])
            box1.delete("1.0",END)
            a = len(left)-1
            left = left[:-1]
            if a >=45:
                box1.insert("1.0",left[-16:])
            else:
                box1.insert("1.0",left[:f]+left[29:])
            if wrong:
                wrong = wrong[:-1]
    selection()

main_frame2 = Frame(root,background="#00dfdf")

main_frame = Frame(root,background="#00dfdf")
main_frame.pack(fill=BOTH,expand=1)

canvas = Canvas(main_frame,width=440,height=150,background="#00dfdf",highlightbackground="dark green")
canvas2 = Canvas(main_frame2,width=440,height=150,background="#00dfdf",highlightbackground="dark green")
canvas.pack(pady=10)
canvas2.pack(pady=10)

canvas.create_text(60,20,text="Time",fill="dark green",font=("Times New Roman",18))
canvas2.create_text(60,20,text="Time",fill="dark green",font=("Times New Roman",18))
canvas.create_oval(12,42,112,142,fill="#ece10f")
canvas2.create_oval(12,42,112,142,fill="#ece10f")
canvas.create_oval(19,49,105,135,fill="light green")
canvas2.create_oval(19,49,105,135,fill="light green")
text1 = canvas.create_text(60,90,text="60",fill="Black",font=("Times New Roman",25))
text4 = canvas2.create_text(60,90,text="60",fill="Black",font=("Times New Roman",25))

canvas.create_text(220,20,text="Speed(/WPM)",fill="dark green",font=("Times New Roman",18))
canvas2.create_text(220,20,text="Speed(/WPM)",fill="dark green",font=("Times New Roman",18))
canvas.create_oval(170,42,270,142,fill="#ece10f")
canvas2.create_oval(170,42,270,142,fill="#ece10f")
canvas.create_oval(177,49,263,135,fill="light green")
canvas2.create_oval(177,49,263,135,fill="light green")
text2 = canvas.create_text(220,90,text="0",fill="black",font=("Times New Roman",25))
text5 = canvas2.create_text(220,90,text="0",fill="black",font=("Times New Roman",25))

canvas.create_text(380,20,text="Accuracy(%)",fill="dark green",font=("Times New Roman",17))
canvas2.create_text(380,20,text="Accuracy(%)",fill="dark green",font=("Times New Roman",17))
canvas.create_oval(330,42,430,142,fill="#ece10f")
canvas2.create_oval(330,42,430,142,fill="#ece10f")
canvas.create_oval(337,49,423,135,fill="light green")
canvas2.create_oval(337,49,423,135,fill="light green")
text3 = canvas.create_text(380,90,text="100",fill="black",font=("Times New Roman",25))
text6 = canvas2.create_text(380,90,text="100",fill="black",font=("Times New Roman",25))

input_frame = Frame(main_frame,background="#00dfdf",bd=0)
input_frame.pack(pady=20)

box1 = Text(input_frame,width=14,height=1,relief=SUNKEN,background="#bcfcf9",font=("Times New Roman",24),foreground="grey")
box1.grid(row=0,column=0)
box2 = Text(input_frame,width=13,height=1,relief=SUNKEN,background="#bcfcf9",font=("Times New Roman",24))
box2.grid(row=0,column=1)
box1.insert("1.0","                             ")

red_font = font.Font(box1,box1.cget("font"))
green_font = font.Font(box1,box1.cget("font"))
red_font.configure(overstrike=True)
box1.tag_configure("Red",background="#fd9393",foreground="#fd0000")
box2.tag_configure("Red",background="#fd9393",foreground="#fd0000")
box1.tag_configure("Strike",font=red_font)
box2.tag_configure("Strike",font=red_font)

box1.tag_configure("Green",font=green_font,background="#89db66",foreground="#80ff00")
box2.tag_configure("Green",font=green_font,background="#89db66",foreground="#80ff00")

label = Label(main_frame,text="",font=("Times New Roman",15))

insert()

root.bind("<Key>",type)
box2.bind("<Button-1>",box2.mark_set("insert","1.0"))

my_menu = Menu(root,tearoff=OFF)
root.config(menu=my_menu)

file_menu = Menu(my_menu,tearoff=OFF)
my_menu.add_cascade(label="Types",menu=file_menu)
file_menu.add_command(label="1-minute Test",command=lambda:change(1))
file_menu.add_command(label="2-minute Test",command=lambda:change(2))
file_menu.add_command(label="5-minute Test",command=lambda:change(3))
file_menu.add_command(label="Paragraph Test",command=para)

root.mainloop()