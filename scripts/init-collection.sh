#!/usr/bin/env bash
set -e

mongo <<EOF
use $DB
db.createUser({
  user:  '$USER',
  pwd: '$PSW',
  roles: [{
    role: 'readWrite',
    db: '$DB'
  }]
})
db.movies.createIndex({ id:"hashed"})
db.credits.createIndex({ movie_id:"hashed"})
sh.enableSharding('$DB')
sh.shardCollection( "$DB.movies", { id:"hashed" })
sh.shardCollection( "$DB.credits", { movie_id:"hashed" })
EOF
