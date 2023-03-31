Name:		texlive-univie-ling
Version:	64772
Release:	2
Summary:	Papers, theses and research proposals in (Applied) Linguistics at Vienna University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/univie-ling
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/univie-ling.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/univie-ling.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides LaTeX2e classes, BibLaTeX files, and
templates suitable for student papers, PhD research proposals
(Exposes), and theses in (Applied) Linguistics at the
University of Vienna. The classes implement some standards for
these types of text, such as suitable title pages. They are
particularly suited for the field of (Applied) Linguistics and
pre-load some packages that are considered useful in this
context. The classes can also be used for General and
Historical Linguistics as well as for other fields of study at
Vienna University. In this case, however, some settings may
have to be adjusted.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/univie-ling
%doc %{_texmfdistdir}/doc/latex/univie-ling

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
