#!/bin/bash
echo "Simple recon script to get all the necessary information about a website using nmap, nikto and recon-ng"
echo "Author: Abhijith P Kumar"

CHOICE="Y"

read -p "Enter the host name: " HOST
while [[ $CHOICE == "Y" || $CHOICE == "y" ]]
do
	echo "Select which tool you want to use:"
	echo "[1] nmap: Scan all TCP ports using default parameters"
	echo "[2] nikto: vulnerability scanner"
	echo "[3] recon-ng: search and enumerate subdomains and important
	files"
	read TOOL
	case $TOOL in
			
		1) echo "Scanning $HOST using nmap..."
		   echo ""
                   nmap -T4 $HOST -oN ${HOST}_nmap.txt
		   ;;

		2) echo ""
		   echo "Scanning $HOST using Nikto..."
		   echo ""
		   nikto -h $HOST > ${HOST}_nikto.txt
		   ;;

	        3) if [[ $(echo $HOST | cut -c1-3) == 'www' ]]
		   then
		        	WEBSITE=$(echo $HOST | cut -d'.' -f 2)
		   else
			        WEBSITE=$(echo $HOST | cut -d'.' -f 1)
		   fi

		  recon-cli -w $WEBSITE -C 'db insert companies $WEBSITE' -C 'db insert domains $HOST' 

		  recon-cli -w $WEBSITE -m recon/domains-hosts/bing_domain_web -o SOURCE=$HOST -x

		  recon-cli -w $WEBSITE -m recon/domains-hosts/brute_hosts -o SOURCE=$HOST

		  recon-cli -w $WEBSITE -m recon/domains-hosts/google_site_web -o SOURCE=$HOST -x

		  recon-cli -w $WEBSITE -m recon/domains-hosts/findsubdomains -o SOURCE=$HOST -x

		  recon-cli -w $WEBSITE -m discovery/info_disclosure/interesting_files -x

		  recon-cli -w $WEBSITE -m reporting/csv -o FILENAME=${pwd}/${WEBSITE}.csv -x
		  ;;
	  *) echo "Please select a valid number"
		  exit
		  ;;
  esac
	echo "All scans completed. Do you want to re-scan using a different tool?[y/n]"
	read CHOICE
done
exit
