# This Praat script will extract all the pitch result of sound files.
# 
# This script is distributed under the GNU General Public License.
# Copyright 2022.03.20 [feipengshao@163.com]

form Information
	comment Directory path of input WAV files:
	text input_wav_directory sample_data/
	comment Path of output result file:
	text save_result_directory result_pitch_Praat/
endform

if (praatVersion < 6001)
	printline Requires Praat version 6.0 or higher. Please upgrade your Praat version 
	exit
endif
createDirectory: save_result_directory$
Create Strings as file list: "fileList", input_wav_directory$ + "*.wav"
numberOfFiles = Get number of strings
for iFile from 1 to numberOfFiles
	selectObject: "Strings fileList"
	fileName$ = Get string: iFile
	Read from file: input_wav_directory$ + fileName$
	objectName$ = selected$ ("Sound", 1)
	save_result$ = save_result_directory$ + objectName$ + ".f0"
	totalTime = Get end time
	To Pitch: 0, 75, 600
	selectObject: "Sound " + objectName$
	Remove

	stepTime = totalTime / 0.005
	for i from 1 to stepTime
			selectObject: "Pitch " + objectName$
			tmpTime = 0.005 * (i - 1)
			pitchValue = Get value at time: tmpTime, "Hertz", "Linear"
			if pitchValue <> undefined
				appendFileLine: save_result$, string$(pitchValue)
			else
				appendFileLine: save_result$, "0.0"
			endif
	endfor

	#appendFileLine: save_result$, output$
	selectObject: "Pitch " + objectName$
	Remove
endfor

selectObject: "Strings fileList"
Remove
exit Done!Thank you!-shaopf