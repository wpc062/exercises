#!/usr/bin/env perl
# perl-grep.pl

my $regex=shift @ARGV
print "Regex is [$regex]\n";

while (<>) {
    print if m/$regex/;
}

