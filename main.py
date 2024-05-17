import json
import gzip
import sys
from datetime import datetime, timezone

def main(input_file):
    visits = []
    hits = []

    def to_iso8601(timestamp):
        return datetime.fromtimestamp(int(timestamp), tz=timezone.utc).isoformat()

    with gzip.open(input_file, 'rt', encoding='utf-8') as f:
        for line in f:
            visit = json.loads(line)

            visit_record = {
                "full_visitor_id": visit["fullVisitorId"],
                "visit_id": visit["visitId"],
                "visit_number": int(visit["visitNumber"]),
                "visit_start_time": to_iso8601(visit["visitStartTime"]),
                "browser": visit["device"]["browser"],
                "country": visit["geoNetwork"]["country"]
            }
            visits.append(visit_record)

            for hit in visit["hits"]:
                hit_timestamp = int(visit["visitStartTime"]) + (int(hit["time"]) // 1000)
                hit_record = {
                    "hit_number": int(hit["hitNumber"]),
                    "hit_type": hit["type"],
                    "hit_timestamp": to_iso8601(hit_timestamp),
                    "page_path": hit.get("page", {}).get("pagePath", ""),
                    "page_title": hit.get("page", {}).get("pageTitle", ""),
                    "hostname": hit.get("page", {}).get("hostname", "")
                }
                hits.append(hit_record)

    with open('visits.json', 'w') as visits_file:
        for visit in visits:
            visits_file.write(json.dumps(visit) + '\n')

    with open('hits.json', 'w') as hits_file:
        for hit in hits:
            hits_file.write(json.dumps(hit) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
