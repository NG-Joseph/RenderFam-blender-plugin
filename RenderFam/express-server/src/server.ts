import express from 'express';
import path from 'path';
const app = express();
const port  = process.env.PORT || 3005;


// start the express server
app.listen( port, () => {
    // tslint:disable-next-line:no-console
    console.log( `server started at http://localhost:${ port }` );
} );



