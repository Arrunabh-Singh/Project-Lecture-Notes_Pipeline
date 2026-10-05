#!/usr/bin/env bash
# Download lecture videos from link-shared Drive copies into the layout cli.py expects:
#   data/lectures/<chapter>/<original-id>/video.<ext>
#
# Why copies: the teacher's own files can't be fetched without Drive OAuth, and the Drive
# connector caps downloads at 10 MB. The agent copies the chapter's videos into a folder in
# the student's own Drive (Drive connector copy_file), the student sets that folder to
# "Anyone with the link", this script pulls them over plain HTTPS, and the agent trashes
# the copies once transcription is done.
#
# The map is a TSV with one line per lecture:
#   original_id <TAB> copy_id <TAB> size_bytes <TAB> mime_type <TAB> title
# Keep it under data/lectures/ (gitignored). This repo is public, and while the folder is
# link-shared, anyone holding the copy ids can download the teacher's recordings.
#
# Usage: tools/fetch_drive_copies.sh leph109 data/lectures/leph109/_copies.tsv
set -u
chapter="$1"; map="$2"
cd "$(dirname "$0")/.."
jar="$(mktemp)"; trap 'rm -f "$jar"' EXIT
ok=0; bad=0
while IFS=$'\t' read -r orig copy size mime title; do
  [ -z "${orig:-}" ] && continue
  ext="${title##*.}"
  dir="data/lectures/$chapter/$orig"; dest="$dir/video.$ext"
  mkdir -p "$dir"
  if [ -f "$dest" ] && [ "$(stat -c%s "$dest")" = "$size" ]; then echo "SKIP ok  $title"; ok=$((ok+1)); continue; fi
  for attempt in 1 2 3; do
    # confirm=t skips Drive's "too large to scan for viruses" page; -C - resumes a partial file.
    curl -sS -L -C - -c "$jar" -b "$jar" -o "$dest" \
      "https://drive.usercontent.google.com/download?id=${copy}&export=download&confirm=t" --max-time 900
    got=$(stat -c%s "$dest" 2>/dev/null || echo 0)
    [ "$got" = "$size" ] && break
    if head -c 200 "$dest" | grep -qi '<html'; then
      echo "  got a web page, not video: the folder is not link-shared"; rm -f "$dest"; break
    fi
    echo "  retry $attempt: have $got of $size"; sleep $((2**attempt))
  done
  got=$(stat -c%s "$dest" 2>/dev/null || echo 0)
  if [ "$got" = "$size" ]; then echo "OK   $(printf '%10d' "$got")  $title"; ok=$((ok+1));
  else echo "FAIL $(printf '%10d' "$got") of $size  $title"; bad=$((bad+1)); fi
done < "$map"
echo "== $ok ok, $bad failed =="
[ "$bad" = 0 ]
