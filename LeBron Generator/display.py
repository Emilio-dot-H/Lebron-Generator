import PySimpleGUIWeb as sg
import legenerator

def main():
	LeTotal = []
	msg_people = """This is a small project in large part dedicated to the r/nba community. This is meant to be taken as light 
	fun and in good spirit. Lebron James is a high-level athlete and a bonafide superstar in the NBA. The play on words originated
	 as a meme where you would that the first part of James' name ("Le") and attach it to a word of your choosing. 

\nWhile this is a project to refine my coding skills, I look to clean it up and add more features to the applications.

\nUpcoming features that I would like to incorporate is a 'Random' feature as well as 'Celebrity/Famous People' feature. 
	"""

	# Define the window's contents
	layout = [[sg.Text(" ")],
			  [sg.Text("Enter word to LeTransform", background_color='#a84747',font='Helvetica 23')],
	          [sg.Input(key='-INPUT-', default_text= "Enter Text..")],
	          [sg.Button(button_text = "Find LeSynonyms",key='Transform', button_color=('white', '#47a86e'))],
	          [sg.Text(" ")],
	          [sg.Text(key='-OUTPUT-', background_color='#a84747', font ='Arial 20')],
	          [sg.Multiline(key='-ML1-',do_not_clear=False, size=(30,10), font=('Arial 18'))],
	          [sg.Button('Clear', button_color=('white','#1c82bd'))],
	          [sg.Text(" ")],
	          [sg.Image('img/jaecrowderlebron.png', size=(400,250)), sg.Image('img/goatbron.png', size=(400,250)), sg.Image('img/lebrontony.png', size=(400,250))],
	          [sg.Text(msg_people, background_color='#a84747',text_color='#e4e673',justification= 'center', font='Helvetica 15', size=(100,5))]]

	#[sg.Button('Transform', button_color=('white', '#47a86e')), sg.Button('Quit', button_color=('white', '#47a86e'))]
	# Create the window
	# window = sg.Window('Window Title', layout, web_port=2222, web_start_browser=False)
	sg.ChangeLookAndFeel('Reddit')
	window = sg.Window('Window Title', layout, background_color='#a84747', element_justification='center',
		resizable=True)

	# Display and interact with the Window using an Event Loop
	while True:
	    event, values = window.read()

	    entry = values['-INPUT-']
	    #FOR GETTING 1ST WORD
	    legenerator.LeTransform(entry, LeTotal)
	    #GET LIST OF SYN
	    synonyms = legenerator.get_synonyms(entry)
	    #GENERATE FOR LIST OF SYN
	    legenerator.LeGenerator(synonyms, LeTotal)
		# See if user wants to quit or window was closed
	    primaries = legenerator.get_primesyn()
	    others = legenerator.get_othersyn()
	    # result =  '\n\n' + '\n'.join([" || ".join(primaries[i:i+3]) for i in range(0,len(primaries),3)]) + '\n---\n' + '\n'.join([" || ".join(others[i:i+3]) for i in range(0,len(others),3)])
	    result = '\n'.join(primaries) + '\n' +'\n'.join(others)
	    error_msg = 'This terms is unavailable in our word bank.\nMake sure that the term is a single word and is spelled correctly. \nSome examples of valid terms: cold, hot, wet, fire'
	    error_msg2 = 'ERROR: Please enter a word'

	    if event == sg.WINDOW_CLOSED or event == 'Quit':
	        break
	    # Output a message to the window
	    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI",
	    #                           text_color='yellow')
	    elif event == 'Transform':
	    	if len(LeTotal)<1:
	        	synonyms=[]
	        	window['-ML1-'].update(error_msg2, append = False)
			
	    	elif synonyms is None:
	            synonyms=[]
	            window['-ML1-'].update(error_msg, append = False)

	    	else:
		    	entry_word = 'Word: ' + LeTotal[0]
		    	window['-OUTPUT-'].update(entry_word)
		    	window['-ML1-'].update(result, append = False, text_color='#3B006B',
		    	    background_color = '#FCF3CF')
	    	LeTotal.clear()
	    	synonyms.clear()
	    	primaries.clear()
	    	others.clear()
	    	result = ''

	    elif event == 'Clear':
	        LeTotal.clear()
	        synonyms.clear()
	        primaries.clear()
	        others.clear()
	        result = ''
	        window['-ML1-'].update(result, append = False)
	        window['-OUTPUT-'].update('LeCleared')

	window.close()

if __name__ == '__main__':
    main()