from google.cloud import storage
import os
import pickle
import glob
from typing import Dict
from .sentences_similarity import SentenceSimilarity

import nltk
from nltk.corpus import wordnet as wn

nltk.download('averaged_perceptron_tagger')

# os.environ["GOOGLE_CLOUD_PROJECT"] = 'climatekaraoke'
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.realpath(__file__)) + '/creds.json'

# def storage_client() -> storage.Client:
#     return storage.Client(credentials='creds.json')


# def list_buckets():
#     """Lists all buckets."""

#     buckets = storage_client().list_buckets()

#     for bucket in buckets:
#         print(bucket.name)


# def list_objects(bucket_name):
#     """Lists all the blobs in the bucket."""

#     blobs = storage_client().list_blobs(bucket_name)

#     for blob in blobs:
#         print(blob.name)


# def dump_dict_to_pickle(dict_filename: str, dictionary: Dict[str, str]) -> str:
#     dictionary_path: str = f'{dict_filename}.pickle'
#     with open(dictionary_path, 'wb') as handle:
#         pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
#     print(f'Saved the dictionary to pickle {dictionary_path}')
#     return dictionary_path


# def download_object(bucket_name,
#                     source_blob_name,
#                     destination_file_name) -> str:
#     """Downloads a blob from the bucket."""

#     bucket = storage_client().bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)
#     blob.download_to_filename(destination_file_name)

#     print(
#         "Object {} downloaded to {}.".format(
#             source_blob_name, destination_file_name
#         )
#     )

#     return destination_file_name


# def upload_object(bucket_name, source_file_name, destination_blob_name):
#     """Uploads a file to the bucket."""

#     bucket = storage_client().bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_filename(source_file_name)

#     print(
#         "File {} uploaded to {}.".format(
#             source_file_name, destination_blob_name
#         )
#     )


# def unpickle_dictionary(dictionary_path: str) -> Dict[str, str]:
#     with open(dictionary_path, 'rb') as handle:
#         unpickled_dict: Dict[str, str] = pickle.load(handle)
#         print(f'Unpickled dict from path {dictionary_path}')
#         return unpickled_dict


# def download_dictionary(gcs_dict_name: str,
#                         bucket_name: str = 'python_directories') -> Dict[str, str]:
#     return unpickle_dictionary(download_object(bucket_name,
#                                                gcs_dict_name,
#                                                f''))


# def create_folder(bucket_name, destination_folder_name):
#     bucket = storage_client().get_bucket(bucket_name)
#     blob = bucket.blob(destination_folder_name)

#     blob.upload_from_string('')

#     print('Created {}'.format(
#         destination_folder_name))


# def upload_folder(directory_path: str, bucket_name: str):
#     dir_name: str = [d for d in directory_path.split('/') if d][-1]
#     create_folder(bucket_name, dir_name)
#     bucket = storage_client().bucket(bucket_name)
#     for fil_path in glob.glob(f'{directory_path}/*'):
#         fil_name: str = fil_path.split('[./]')[-1]
#         blob = bucket.blob(f'{dir_name}{fil_name}')
#         blob.upload_from_filename(fil_path)
#         print(f'Uploaded {fil_path}')


# def download_folder(directory_name: str, bucket_name: str):
#     bucket = storage_client().bucket(bucket_name)
#     blobs = bucket.list_blobs(prefix=directory_name)
#     for blob in blobs:
#         if (not blob.name.endswith("/")):
#             try:
#                 os.makedirs("/".join(blob.name.split('/')[:-1]))
#             except FileExistsError:
#                 pass
#             blob.download_to_filename(blob.name)


import prosodic as p
import pronouncing
import nltk
from nltk.corpus import wordnet as wn


import os

p.config['print_to_screen']=0

TEXTFILES = ["lyrics.txt", "autogen1.txt",'Combined_lyrics_gathered.txt']

# for file_name in TEXTFILES:
#   if not os.path.isfile(file_name):
# 	  download_object("lyrics_text_files", file_name, file_name)

PHON_MAP = {"iː": "0", "uː": "1", "e": "2", "ə": "3", "a": "4", "o": "5", "ɛ": "6", \
   "ʌ": "7", "ɑ": "8", "æ": "9", "ɪ": "A", "ɛː": "B", "ʊ": "C", "3": "D", "ɔː": "E", \
    "ɔ": "F", "ʉː": "G"}

PHONE_DEFAULT = "ə"
STRESS_DEFAULT = "H"

def make_dicts (filename):

   stress_dict = dict()
   phones_dict = dict()
   token_dict = dict()

   for file_name in TEXTFILES:

      t = p.Text(os.path.dirname(os.path.realpath(__file__)) + "/" + file_name)

      for line in t.lines():
         token = p.Text(str(line)) 
         syl = token.syllables()

         weightstr = ""
         phonestr = ""

         for s in syl:
            weight = s.str_weight()
            weightstr = weightstr + weight

            vowel = str(s.getVowel())
            if vowel in PHON_MAP:
               phonestr = phonestr + str(PHON_MAP[vowel])
            else:
               phonestr = phonestr + vowel

         text = str(token.lines()[0]).lower()

         # handling of words which are not in the prosodic dictionary
         syllables_total = [t for t in token.words()]
         syllables_recovered = [t for t in token.words() if len(t.syllables()) > 0]
         num_syllables_total = len(syllables_total)
         num_syllables_recovered = len(syllables_recovered)

         if num_syllables_recovered < num_syllables_total:
            matches = [s1 == s2 for s1, s2 in zip(syllables_total[0:num_syllables_recovered], \
               syllables_recovered)]
            pos_list = [i for i,m in enumerate(matches) if m == False]
            if len(pos_list) > 0:
               pos = pos_list[0]
               weightstr = weightstr[:pos] + STRESS_DEFAULT + weightstr[pos:]
               phonestr = phonestr[:pos] + PHON_MAP[PHONE_DEFAULT] + phonestr[pos:]
            else:
               weightstr = weightstr + STRESS_DEFAULT
               phonestr = phonestr + PHON_MAP[PHONE_DEFAULT]
         

         if not weightstr in stress_dict:
            stress_dict[weightstr] = []

         if text not in stress_dict[weightstr]:
            stress_dict[weightstr].append(text)

         if not phonestr in phones_dict:
            phones_dict[phonestr] = []

         if text not in phones_dict[phonestr]:
            phones_dict[phonestr].append(text)
            
         # fill token dict
         if num_syllables_total not in token_dict:
            token_dict[num_syllables_total] = dict()

         if weightstr not in token_dict[num_syllables_total]:
            token_dict[num_syllables_total][weightstr] = dict()

         if phonestr not in token_dict[num_syllables_total][weightstr]:
            token_dict[num_syllables_total][weightstr][phonestr] = []

         token_dict[num_syllables_total][weightstr][phonestr].append(text)
            
   return stress_dict, phones_dict, token_dict

stress_dict, phones_dict, token_dict = make_dicts("lyrics.txt")

import random

def closest_strings(strlist, token):
    max_matches = 0
    strings = []
    for s in strlist:
        matches = sum(a==b for a, b in zip(s, token))
        if matches > 0 and matches == max_matches:
            strings.append(s)
        elif matches > max_matches:
            max_matches = matches
            strings = [s]
    return strings

def get_chunks(number_token,token_dict):
  random_first_chunck=0
  second_random_chunk=0
  while True:
    
    random_first_chunck= random.choice(list(token_dict.keys()))
    if random_first_chunck < number_token:
      second_random_chunk = number_token- random_first_chunck
    if second_random_chunk in token_dict and random_first_chunck in token_dict:
      break
  return random_first_chunck, second_random_chunk
def merge_final_result(original_song, list_new_key_words):
  final_res=''
  t = p.Text(original_song)
  for sen in t.lines():
    sent = str(sen).lower()
    for new_sen, original in list_new_key_words:
      # print(sent, original )
      if original==sent or original in sent or sent in original :
        # print('here')
        final_res+=new_sen
        final_res+='\n '
        break
  return final_res
def get_new_sentnce(number_token,token_dict,token_dict_test_case,stress_dict, original_token):
  
      for stress_ in stress_dict:
        ###### check if stress exist in our lyrics DB
        if stress_ in token_dict[number_token]:
          phoneme_found=False
          ######  check for phonesms if it doesn't exist return random one, else return any one will do later
          phonatic_dict=stress_dict[stress_]
          original_sen=''
          for phoneme in phonatic_dict:
            original_sen = token_dict_test_case[original_token][stress_][phoneme][0]
            if phoneme in token_dict[number_token][stress_]:

              return token_dict[number_token][stress_][phoneme][0], original_sen
              phoneme_found= True
              break
          ##### if we couldn't find phoneme just select randomly
          if phoneme_found== False:            
            return token_dict[number_token][stress_][random.choice(list(token_dict[number_token][stress_].keys()))][0], original_sen
            phoneme_found= True
        ####### if given stress doesnt exist then we randomize
        else:
          original_sen=''
          phonatic_dict=stress_dict[stress_]
         
          for phoneme in phonatic_dict:
            original_sen = token_dict_test_case[original_token][stress_][phoneme][0]
            
          random_stress_list= closest_strings (token_dict[number_token],stress_dict[stress_])
          random_stress=random.choice(list(token_dict[number_token].keys()))
          # random_stress=random.choice(list(token_dict[number_token].keys()))         
          return token_dict[number_token][random_stress][random.choice(list(token_dict[number_token][random_stress].keys()))][0], original_sen


def generate_new_lyrics(old_song):
  final_lyrics=''
  stress_dict_test_case, phones_dict_test_case, token_dict_test_case=make_dicts_2(old_song)
  new_generated_lyrics=[]
  for set_test_case in token_dict_test_case:  
    number_token=set_test_case
    #### First Case if number of tokens exist
    if number_token  in token_dict:
      ### get stress to compare
      stress_dict= token_dict_test_case[set_test_case]
      new_generated_lyrics.append(get_new_sentnce(number_token,token_dict,token_dict_test_case,stress_dict,number_token))
      
    ### if we dont find matching number of tokens then divide and conquer + sentenec similarityy
    else:
      stress_dict= token_dict_test_case[set_test_case]
      str_final_result = match_longer_sentnces(number_token,token_dict_test_case,token_dict,stress_dict)
      for sen, original in  str_final_result:
        new_generated_lyrics.append((sen,original))



  final_lyrics=merge_final_result(old_song,new_generated_lyrics)
  return final_lyrics

def make_dicts_2 (filename):

   t = p.Text(filename)

   stress_dict = dict()
   phones_dict = dict()
   token_dict = dict()

   for line in t.lines():
      token = p.Text(str(line)) 
      syl = token.syllables()

      weightstr = ""
      phonestr = ""

      for s in syl:
         weight = s.str_weight()
         weightstr = weightstr + weight

         vowel = str(s.getVowel())
         if vowel in PHON_MAP:
            phonestr = phonestr + str(PHON_MAP[vowel])
         else:
            phonestr = phonestr + vowel

      text = str(token.lines()[0]).lower()

      # handling of words which are not in the prosodic dictionary
      syllables_total = [t for t in token.words()]
      syllables_recovered = [t for t in token.words() if len(t.syllables()) > 0]
      num_syllables_total = len(syllables_total)
      num_syllables_recovered = len(syllables_recovered)

      if num_syllables_recovered < num_syllables_total:
         matches = [s1 == s2 for s1, s2 in zip(syllables_total[0:num_syllables_recovered], \
            syllables_recovered)]
         pos_list = [i for i,m in enumerate(matches) if m == False]
         if len(pos_list) > 0:
            pos = pos_list[0]
            weightstr = weightstr[:pos] + STRESS_DEFAULT + weightstr[pos:]
            phonestr = phonestr[:pos] + PHON_MAP[PHONE_DEFAULT] + phonestr[pos:]
         else:
            weightstr = weightstr + STRESS_DEFAULT
            phonestr = phonestr + PHON_MAP[PHONE_DEFAULT]
         

      if not weightstr in stress_dict:
         stress_dict[weightstr] = []

      if text not in stress_dict[weightstr]:
         stress_dict[weightstr].append(text)

      if not phonestr in phones_dict:
         phones_dict[phonestr] = []

      if text not in phones_dict[phonestr]:
         phones_dict[phonestr].append(text)
            
      # fill token dict
      if num_syllables_total not in token_dict:
         token_dict[num_syllables_total] = dict()

      if weightstr not in token_dict[num_syllables_total]:
         token_dict[num_syllables_total][weightstr] = dict()

      if phonestr not in token_dict[num_syllables_total][weightstr]:
         token_dict[num_syllables_total][weightstr][phonestr] = []

      token_dict[num_syllables_total][weightstr][phonestr].append(text)
            
   return stress_dict, phones_dict, token_dict

   ##### have stupid bug, i will fix it later
def match_longer_sentnces(number_token,token_dict_test_case,token_dict,stress_dict):
  str_final_result=[]  
  
  for stress_ in stress_dict:
    while True:
      
      #### randomly generate number and check if 2 chuncks exist as syllables then

      random_first_chunck, second_random_chunk= get_chunks(number_token,token_dict)
      
      ### we will do similar to that we have done in previos could 'Main algorithm', bu the difference we have to check similarity
      setnece1, _= get_new_sentnce(random_first_chunck,token_dict,token_dict_test_case,stress_dict, number_token)
      setnece2, original_sen = get_new_sentnce(second_random_chunk,token_dict,token_dict_test_case,stress_dict, number_token)
      # print(setnece1)
      # print(setnece2)
      obj = SentenceSimilarity() 

      try:
        if setnece2!= None and setnece1!= None and obj.main(setnece2,setnece1)> 0.5:
          str_final_result.append((setnece1+" "+setnece2, original_sen)  )
          break
      except:
        print('random error')
    return str_final_result