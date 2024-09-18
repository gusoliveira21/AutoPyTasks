import os

def remove_copyright_text_from_files(base_path):
    copyright_text = """
/*
 * Copyright 2020 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                if copyright_text in content:
                    content = content.replace(copyright_text, "")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Removed copyright text from: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {str(e)}")

if __name__ == "__main__":
    uri = input("Enter the URI path: ")
    remove_copyright_text_from_files(uri)
