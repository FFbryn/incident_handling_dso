# Incident Handling – DevSecOps

## Deskripsi
Project ini merupakan simulasi Incident Handling end-to-end pada lingkungan DevSecOps
dengan studi kasus **Brute Force Login Attack** pada aplikasi web Flask.

## Lingkungan
- Proxmox Server: 10.10.93.47
- VM Ubuntu Server 22.04
- Flask Web Application
- ELK Stack (Elasticsearch, Logstash/Filebeat, Kibana)
- Prometheus & Grafana

## Skenario Insiden
Brute force login attack dengan login gagal berulang dari IP yang sama
dalam waktu singkat.

## Tahapan Incident Response
1. Preparation
2. Identification (ELK & Grafana)
3. Containment (iptables)
4. Eradication (patch & reset)
5. Recovery
6. Lessons Learned

## Output
- Screenshot log Kibana
- Screenshot dashboard Grafana
- Incident Report (PDF)
- Artikel dokumentasi insiden

## Author
Surya Febriyan  
Mata Kuliah DevSecOps
