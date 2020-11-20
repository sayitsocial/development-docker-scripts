export $(xargs < .env)

DIR=$PWD

cd $WORKDIR
echo "Fetching"
if ! git fetch $DEVELOPMENT_REMOTE > $DIR/fetch.log; then 
    exit 1
fi
echo "Fetched from $DEVELOPMENT_REMOTE"
echo "Pulling"
if ! git pull $DEVELOPMENT_REMOTE $DEVELOPMENT_BRANCH > $DIR/pull.log; then
    exit 1
fi
echo "Pulled from $DEVELOPMENT_BRANCH"

if ! git submodule update --init > $DIR/submodule.log; then
    exit 1
fi
cd $DIR
exit 1
