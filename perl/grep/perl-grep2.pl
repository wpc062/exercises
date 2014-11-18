#!/usr/bin/env perl
# perl-grep.pl

my $pattern = shift @ARGV;

my $regex = eval { qr/$pattern/ };
die "Check your pattern! $@" if $@;

while (<>) {
    print if m/$regex/;
}

