# JsonAssist
JsonAssist is an open-source library for Python, designed to enhance the user experience with JSON files. <br>It provides convenient features for reading, writing, and easily manipulating JSON data.

# USAGE


	{
		"config":  {
			"title":  "Default Configuration",
			"default-ip":  "127.0.0.1",
			"default-interface":  "eth0",
			"author":  "rapido"
		}
	}
(config.json)

-------

 - *is_file_exist(file)* : Test if the json file exists 
 > Take json file in argument
----
 - *get_data_of_file(file)* : Return the content of json file to use it after  take json file in argument
 > Take json file in argument
 ----
 - *get_all_key(file)* : Return keys in the json file, exemple "title, default-ip"...  
 > Take json file in argument
----
- *get_value_of_key(file)* : Return value of every keys in the json file, exemple "Default Configuration, 127.0.0.1"... 
 > Take json file in argument
 ----
- *check_value_of_one_key(file,  val)* : Return if a value exists with a key, exemple "config.json, rapido"
> Take json file and value in argument
----
- *check_one_key_in_file(file,  key)* : Return if a key exists in the json file, exemple "config.json, author"
> Take json file and key in argument 
----
- *change_value_of_key(file,  key,  new_val)* : Change a value of a key in the json file, exemple "config.json, author, laetc"
> Take json file valid key and value  
