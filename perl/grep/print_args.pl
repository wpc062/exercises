#!/usr/bin/env perl
# perl-grep4.pl

sub print_args
{
    print "param list:";
    foreach (@_)
    {
        print "\t$_";
    }
    print "\n";
}

sub print_args2
{
    print "param list:";
    $str = join("\t", @_);
    print "\t", $str, "\n";
}

sub print_args3
{
    print "param list:";
    #@_ = sort @_;
    $_ = shift;
    while (defined $_)
    {
        print "\t$_";
        $_ = shift;
    }
    print "\n";
}

print "program: $0\n";

print_args(@ARGV);
print_args2(@ARGV);
print_args3(@ARGV);

print "param list: @ARGV\n"

