for commit in `git rev-list --all`; do
    git log -n 1 --pretty=%ad $commit
    git archive $commit partI.tex partII.tex | wc -c
done