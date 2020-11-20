export $(xargs < .env)

DIR=$PWD

cd $WORKDIR

make down > $DIR/makedown.log
if make pull && make build > $DIR/makeup.log; then 
    exit 1
fi

cd $DIR
