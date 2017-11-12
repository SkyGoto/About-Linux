#！/bin/bash
files=`ls -U /home/sky_human/BackGrounds | grep -v contest | tr " " "+"`
last_file='empty'

echo '<background>'
echo '	<starttime>'
echo '	 <year>2017</year>'
echo '	 <month>11</month>'
echo '	 <day>12</day>'
echo '	 <hour>00</hour>'
echo '	 <minute>00</minute>'
echo '	 <second>00</second>'
echo '	</starttime>'

for current_file in $files
do
    if [[ $last_file == 'empty' ]]
    then
	last_file=$current_file
	echo ' <static>'
	echo '	<duration>300.0</duration>'
	echo "	<file>/home/sky_human/BackGrounds/`echo ${last_file}| tr "+" " "`</file>"
	echo ' </static>'
     else
	echo ' <transition>'
	echo '	<duration>5.0</duration>'
	echo "  <from>/home/sky_human/BackGrounds/`echo ${last_file}| tr "+" " "`</from>"
	echo "  <to>/home/sky_human/BackGrounds/`echo ${current_file}| tr "+" " "`</to>"
	echo ' </transition>'
	echo ' <static>'
	echo '  <duration>300.0</duration>'
	echo "  <file>/home/sky_human/BackGrounds/`echo ${current_file}| tr "+" " "`</file>"
	echo ' </static>'
	last_file=$current_file
      fi
done

echo '</background>'
