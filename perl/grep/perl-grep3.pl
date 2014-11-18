#!/usr/bin/env perl
# perl-grep3.pl

my $pattern = shift @ARGV;

my $regex = eval { qr/$pattern/ };
die "Check your pattern! $@" if $@;

while (<>) {
    print "$_\t\tmatched >>>$&<<<\n" if m/$regex/;
}

