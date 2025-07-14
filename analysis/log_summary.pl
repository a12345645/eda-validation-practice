#!/usr/bin/perl
use strict;
use warnings;

my $file = $ARGV[0];
open my $fh, '<', $file or die "Cannot open $file: $!";

my ($warn, $err) = (0, 0);

while (<$fh>) {
    $warn++ if /WARNING/i;
    $err++  if /ERROR/i;
}

print "Log file: $file\n";
print "Warnings: $warn\n";
print "Errors: $err\n";
