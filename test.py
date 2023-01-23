import openai
import os


import os
import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Brainstorm some ideas combining VR and fitness:\n\n1. Virtual Reality Gym: A virtual reality gym that allows users to experience a realistic and immersive workout environment from their own homes.\n2. VR Personal Trainer: A personal trainer who guides you through a VR fitness routine, providing real-time feedback and encouraging motivation throughout the session.\n3. Interactive Fitness Games: Interactive games that use motion controllers and headsets to create an engaging and fun workout experience for players of all ages.\n4. VR Yoga Studio: An online yoga studio with pre-recorded classes in various styles, allowing users to practice at home with guidance from experienced instructors in a 3D environment. \n5. Movement Tracking App: An app that uses sensors attached to your body or clothing to track your movements while exercising",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
