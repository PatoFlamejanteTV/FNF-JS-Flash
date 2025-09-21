import os
from pydub import AudioSegment

# Base folder (change this)
base_folder = r"C:\\Users\\mcmco\\FNF-JS-Flash\\assets"

count = 0
for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith(".ogg"):
            file_path = os.path.join(root, file)
            count += 1
            print(f"[{count}] 🔄 Compressing: {file_path}")

            try:
                # Load audio
                audio = AudioSegment.from_ogg(file_path)

                # Resample to 22050 Hz
                audio = audio.set_frame_rate(22050)

                # Export back, overwriting original
                audio.export(file_path, format="mp3", bitrate="128k")

                print(f"    ✅ Done: {file_path}\n")

            except Exception as e:
                print(f"    ❌ Error processing {file_path}: {e}\n")

print(f"🎵 Finished! {count} OGG files compressed to 22050 Hz.")
