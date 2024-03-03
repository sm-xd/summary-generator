# main.py (python example)

import os
import json
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)

load_dotenv()

# URL to the audio file
# AUDIO_URL = {
#     "url": "https://www.youtube.com/watch?v=KbzGy3whpy0"
# }
AUDIO_FILE = "test.mp3"

API_KEY = os.getenv("DG_API_KEY")






def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }


        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            summarize="v2",
        )

        # STEP 3: Call the transcribe_url method with the audio payload and options
        # response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)


        # STEP 4: Print the response
        student_details = json.loads(response.to_json(indent=4))
        keysList = list(student_details["results"].keys())
        # print(response.to_json(indent=4))
        print(student_details["results"]["summary"]["short"])
        # print(keysList)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
