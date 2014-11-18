#!/usr/bin/env perl
# perl-grep4.pl

my $pattern = shift @ARGV;

my $regex = eval { qr/$pattern/ };
die "Check your pattern! $@" if $@;

while (<>) {
    if ( m/$regex/ ) 
    {
        print "$_";
        print "\t\t\$&: ",
            substr($_, $-[0], $+[0] - $-[0]),
            "\n";
        foreach my $i (1 .. $#+)
        {
            print "\t\t\$$i: ",
                substr($_, $-[$i], $+[$i] - $-[$i]),
                "\n";

        }
    }
}

