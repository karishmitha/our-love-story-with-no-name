import streamlit as st
import os

st.set_page_config(page_title="Our Story ❤️", layout="centered")

# -------------------- STYLE --------------------

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#000000,#1a0000,#4d0000,#8b0000);
color:white;
font-family: 'Georgia', serif;
}

/* Floating hearts animation */
@keyframes float {
0%{transform:translateY(0px);}
50%{transform:translateY(-20px);}
100%{transform:translateY(0px);}
}

.heart{
position:fixed;
bottom:0;
font-size:25px;
animation:float 4s infinite;
opacity:0.6;
}

.title{
font-size:65px;
text-align:center;
font-weight:bold;
background: linear-gradient(90deg,#ff004c,#ff6600,#ffcc00);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
font-size:28px;
margin-bottom:30px;
color:#ffb3c6;
}

.storybox{
font-size:22px;
line-height:1.9;
background:rgba(255,255,255,0.08);
padding:35px;
border-radius:20px;
box-shadow:0px 10px 40px rgba(0,0,0,0.8);
margin-top:20px;
}

.finalletter{
font-size:24px;
line-height:2;
background:rgba(255,255,255,0.15);
padding:45px;
border-radius:20px;
box-shadow:0px 10px 50px rgba(0,0,0,0.9);
color:#ffd6e0;
}

img{
border-radius:20px;
box-shadow:0px 10px 40px rgba(0,0,0,0.9);
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- MUSIC --------------------
st.markdown("""
<audio autoplay loop>
<source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------------- SECRET QUESTIONS ----------------
correct1="park"
correct2="first kiss"
correct3="papa"

if "unlocked" not in st.session_state:
    st.session_state.unlocked=False

# ---------------- OPENING PAGE ----------------
if not st.session_state.unlocked:

    st.markdown("<div class='title'>Our Journey Begins Here ❤️</div>", unsafe_allow_html=True)
    st.write("Only someone special can unlock this story.")

    q1=st.text_input("Where did we first meet properly?")
    q2=st.text_input("What was our first romantic moment?")
    q3=st.text_input("what is the name you kept for me?")

    if st.button("Unlock Our Story ❤️"):

        if q1.lower()==correct1 and q2.lower()==correct2 and q3.lower()==correct3:
            st.session_state.unlocked=True
            st.rerun()
        else:
            st.error("Only the right person knows these answers ❤️")

# ---------------- STORY PAGE ----------------
else:

    st.markdown("<div class='title'>Our Story</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A Journey Written by the Heart</div>", unsafe_allow_html=True)

    stories = [

"""Chapter 1 – First Glance

Sometimes
life changes in a second…
without any warning.

Among a crowd of people,
my eyes found you.

I didn’t know your name.
I didn’t know your story.

But something in that moment
felt strangely familiar.

You stood there quietly
in your light brown shirt,
and I stood there in my black dress.

Just one glance…
yet my heart whispered,
“Something beautiful
is about to begin.”
""",

"""Chapter 2 – Name Discovery

The world was still the same,
but suddenly we weren’t strangers anymore.

A simple question.
A simple answer.

“What’s your name?”

But the way we laughed,
the way we spoke,
made that moment feel
more special than it should have been.
""",

"""Chapter 3 – Insta Connection

Days passed.
But something inside me
kept thinking about you.

Then suddenly
our conversations began.

Late night messages,
random talks,
small jokes.

A simple “hi”
turned into long conversations.
""",

"""Chapter 4 – First Meeting in the Park

The first time we met properly,
my heart was louder than my words.

The park looked normal to the world.
But for me,
it became a memory.

We walked slowly,
talked endlessly,
laughed without realizing time.
""",

"""Chapter 5 – First Kiss in the Car

That day
something changed forever.

We were sitting in the car,
talking like always.

Then suddenly
everything became quiet.

You stopped the car.
Our eyes met.

And slowly…
we shared our first kiss.
""",

"""Chapter 6 – Small Moments Together

Movie dates.
Shopping trips.
Random walks.

Long talks about nothing
and everything.

But every moment
felt special.

Because
it was with you.
""",

"""Chapter 7 – The Hug That Taught Love

One day
you hugged me.

In that moment
I felt safe.

Your arms became a place
where my heart felt calm.

And somewhere in that hug
I realized quietly…

I was falling in love with you.
""",

"""Chapter 8 – Admiring Him

Your light brown eyes.
Your serious eyebrows.
Your messy hair.

The way you smiled.
The way you listened.

More than your looks,
I admired your heart.
""",

"""Chapter 9 – Our Little World

We built
our own little world.

Holding hands while walking.
Sitting close in parks.

Talking for hours
like time didn’t exist.
""",

"""Chapter 10 – Respect, Care & Motivation

You encouraged me.
You listened to my worries.

Sometimes
you valued me
more than I valued myself.
""",

"""Chapter 11 – The Night Ride & Street Hug

One night
we rode together on your bike.

The wind was cold.
The streets were quiet.

When the ride ended,
we hugged tightly.

That moment
felt like time had stopped.
""",

"""Chapter 12 – Intimate Memories at Home

You feeding me food
like I was a child.

Laughing,
hugging,
being silly.

Those memories
became pieces of happiness
I will always keep.
""",

"""Chapter 13 – The Unexpected Visit

One day
when I was at my part-time work…

you suddenly came.

Seeing you there
made my heart jump with happiness.
""",

"""Chapter 14 – Love Only I Could See

Maybe you never said
the word “love”.

But in my heart
I could see it.
""",

"""Chapter 15 – Accident & Hospital Scene

You met with an accident.

I wore a white coat
like a doctor
just to see you.

Before leaving
I kissed your forehead.

That moment
showed me
how deeply I loved you.
""",

"""Chapter 16 – Distance & Realization

Distance slowly entered our story.

But one thing never changed.

My love for you.
""",

"""Chapter 17 – Waiting for you papa 

papa i am hear to wait for you with
A whole year full of memories.

From the first glance
to every hug, kiss, laugh and tear.

You were never just a person in my life.

You were a story.

A beautiful story
my heart will never forget.
""",

"""❤️ Final Letter

My Dearest,

If you are reading this now,
know that my heart has quietly been with you
through every moment—through your smiles,
your struggles, and even the silence.

I don’t need you to love me back.
My love for you is not a demand or expectation.
It is a gentle, constant light
that will always shine for you, freely and patiently.

I see your worries, your pain, and the challenges you face.
Even from afar, I pray every day—
for your happiness, your peace,
and your heart to be free from burden.

You are stronger than you realize,
braver than you feel,
and capable of more than you imagine.
And in the moments when life feels heavy,
I hope you remember:
someone is always quietly cheering for you,
believing in you, and wishing for your joy.

I will love you always—not to possess, not to expect anything—but simply to celebrate you,
to hold our memories close, and to hope for your happiness.
No matter the distance, no matter the time,
a part of my heart will always belong to you.

With all the love my heart can hold,
Always.
"""
]

    images=[
"images/chapter1.jpg.png",
"images/chapter2.jpg.png",
"images/chapter3.jpg.png",
"images/chapter4.jpg.png",
"images/chapter5.jpg.png",
"images/chapter6.jpg.png",
"images/chapter7.jpg.png",
"images/chapter8.jpg.png",
"images/chapter9.jpg.png",
"images/chapter10.jpg.jpg",
"images/chapter11.jpg.png",
"images/chapter12.jpg.png",
"images/chapter13.jpg.png",
"images/chapter14.jpg.png",
"images/chapter15.jpg.png",
"images/chapter16.jpg.png",
"images/chapter17.jpg.jpg"
]

    if "chapter" not in st.session_state:
        st.session_state.chapter=0

    # ---------------- Chapter Backgrounds ----------------
    if st.session_state.chapter < 10:
        st.markdown("<style>body{background: linear-gradient(135deg,#00008B,#FF69B4);}</style>", unsafe_allow_html=True)
    else:
        st.markdown("<style>body{background: linear-gradient(135deg,#000000,#8B0000);}</style>", unsafe_allow_html=True)

    # ---------------- Display Image ----------------
    if st.session_state.chapter < len(images):
        st.image(images[st.session_state.chapter], use_container_width=True)

    # ---------------- Display Story ----------------
    if st.session_state.chapter == len(stories)-1:
        st.markdown(f"<div class='finalletter'>{stories[st.session_state.chapter]}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='storybox'>{stories[st.session_state.chapter]}</div>", unsafe_allow_html=True)

    # ---------------- Navigation ----------------
    col1,col2=st.columns(2)

    with col1:
        if st.button("⬅ Previous") and st.session_state.chapter>0:
            st.session_state.chapter-=1
            st.rerun()

    with col2:
        if st.button("Next ➡") and st.session_state.chapter < len(stories)-1:
            st.session_state.chapter+=1
            st.rerun()