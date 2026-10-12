# JavaScript Web Scraping

Scripts using the `request` module, UTF-8 file I/O and async callbacks.

| File | Description |
|---|---|
| `0-readme.js` | Reads and prints file content in UTF-8, prints error object on failure |
| `1-writeme.js` | Writes string to file in UTF-8, prints error object on failure |
| `2-statuscode.js` | Prints `code: <status code>` for a GET request (`request`) |
| `3-starwars_title.js` | Prints Star Wars film title via `https://swapi-api.alx-tools.com/api/films/:id` |
| `4-starwars_count.js` | Counts films featuring Wedge Antilles (character ID 18) |
| `5-request_store.js` | Stores webpage body response in a UTF-8 file |
| `6-completed_tasks.js` | Counts completed tasks by `userId` from `https://jsonplaceholder.typicode.com/todos` |

Requires `request` (`npm install request`). All scripts use `#!/usr/bin/node`,
are executable, and end with a newline.
