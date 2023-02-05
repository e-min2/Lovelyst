positive_affirmations = ["I am successful.", 
                         "I am confident", 
                         "I am filled with focus.",
                         "I am strong.",
                         "I am inspiring people through my work."]

body_image = ["I respect my body.",
              "I am comfortable in my own skin.",
              "I take care of my body.",
              "My body is perfect for me.",
              "I give my body what it needs."]

anxiety = ["I am safe and in control.",
           "I have survived my anxiety before. I will survive it now.",
           "I act with confidence because I know what I am doing.",
           "I am capable and prepared.",
           "This feeling is only temporary."]

personal_growth = ["I’m not stopping until I’m the best I can be.",
           "Challenges won’t hold me down.",
           "I am improving for me.",
           "There are always opportunities for me to grow.",
           "Everything I need for success is already here."]

happiness = ["I am creating happiness within myself.",
           "I deserve to be happy.",
           "I am vigorous, energetic, and full of vitality.",
           "I am cultivating a beautiful life free of stress, worries, or fear.",
           "I am proud of my journey and how far I’ve come."]

affirmations = [positive_affirmations, body_image, anxiety, personal_growth, happiness]

select_category = random.randint(0, 5)
select_affirmation = random.randint(0, 5)
    
