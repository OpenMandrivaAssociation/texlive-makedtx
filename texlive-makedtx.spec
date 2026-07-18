%global tl_name makedtx
%global tl_revision 77871
%global tl_bin_links makedtx:%{_texmfdistdir}/scripts/makedtx/makedtx.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Perl script to help generate dtx and ins files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/makedtx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(makedtx.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The makedtx bundle is provided to help LaTeX2e developers to write the
code and documentation in separate files, and then combine them into a
single .dtx file for distribution. It automatically generates the
character table, and also writes the associated installation (.ins)
script.

