#!/bin/bash
EXCLUDE_FILE="README.md"

for FILE in *
do
	if[ -f "$FILE" ] && [ "$FILE" != "$EXCLUDE_FILE" ]; then
		chmod +x "$FILE"
	fi
done
