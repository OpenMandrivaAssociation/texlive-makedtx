Name:		texlive-makedtx
Version:	46702
Release:	2
Summary:	Perl script to help generate dtx and ins files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/makedtx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The makedtx bundle is provided to help LaTeX2e developers to
write the code and documentation in separate files, and then
combine them into a single .dtx file for distribution. It
automatically generates the character table, and also writes
the associated installation (.ins) script.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/makedtx
%{_texmfdistdir}/tex/latex/makedtx
%doc %{_texmfdistdir}/doc/support/makedtx
#- source
%doc %{_texmfdistdir}/source/support/makedtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar texmf-dist/* %{buildroot}%{_texmfdistdir}
