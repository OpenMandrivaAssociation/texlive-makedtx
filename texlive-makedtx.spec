# revision 15878
# category Package
# catalog-ctan /support/makedtx
# catalog-date 2007-10-18 16:19:02 +0200
# catalog-license lppl
# catalog-version 0.94b
Name:		texlive-makedtx
Version:	0.94b
Release:	1
Summary:	Perl script to help generate dtx and ins files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/makedtx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makedtx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The makedtx bundle is provided to help LaTeX2e developers to
write the code and documentation in separate files, and then
combine them into a single .dtx file for distribution. It
automatically generates the character table, and also writes
the associated installation (.ins) script.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makedtx/creatdtx.sty
%doc %{_texmfdistdir}/doc/latex/makedtx/CHANGES
%doc %{_texmfdistdir}/doc/latex/makedtx/README
%doc %{_texmfdistdir}/doc/latex/makedtx/creatdtx.perl
%doc %{_texmfdistdir}/doc/latex/makedtx/makedtx-manual.html
%doc %{_texmfdistdir}/doc/latex/makedtx/makedtx.pdf
%doc %{_texmfdistdir}/doc/latex/makedtx/makedtx.pl
#- source
%doc %{_texmfdistdir}/source/latex/makedtx/makedtx.dtx
%doc %{_texmfdistdir}/source/latex/makedtx/makedtx.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
