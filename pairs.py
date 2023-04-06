pairs = [
    [
        r"Hello, my name is (.*)",
        ["Hello %1, How are you today?","Nice to meet you %1. How is your day going?"]
    ],

    [ 
        r"I'm doing alright|my day is going great",
        ["Good to know, We do have a range of products in our store"]
    ], 
    
    [
        r"What products do you have?",
        ["Our specialty is dealing with electronics. Televisions, Microwaves, Fridges and Washing Machines are all available in the store. which one interests you ?"]
    ],

    [
        r"I would like a television",
        ["Alright, which tv brand is of interest to you ?"]
    ],

    [
        r"My brand of choice is Samsung, the RU7300 model, how much is it?",
        ["That model goes for about 60,000sh ",]
    ],

    [
        r"Great, good to know. which payment options are available?",
        ["We accept both credit and debit cards, M-pesa is also available as a payment option ",]
    ],

    [
        r"I'll pay via mpesa, what are your store's details?",
        ["The mpesa details are: Paybill number is 678123 , Account name: Mecury"]
    ],

    [
        r"I have sent the cash, have you guys received it?",
        ["Indeed we recieved your payment for the samsung television ",]
    ],
    [
        r"Excellent, when will my tv be delivered?",
        ["By next week on a given date at around 5pm, Our delivery agent will bring your product to your residence",]

    ],
    [
        r"That's great, am looking foward to it. Anyways thank you for assisting me in my purchase",
        ["you are very welcome, feel free to shop with us anytime :) Enter quit to end this conversation ",]

    ],  
    [
        r"quit",
        ["It was nice talking to you. See you soon :)"]
],
]
