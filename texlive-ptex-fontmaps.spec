Name:		texlive-ptex-fontmaps
Version:	59711
Release:	1
Summary:	Font maps and configuration tools for Japanese/Chinese/Korean fonts with (u)ptex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ptex-fontmaps
License:	pd gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fontmaps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fontmaps.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fontmaps.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides font maps and setup tools for Japanese,
Korean, Traditional Chinese, and Simplified Chinese. It is the
successor of the jfontmaps package. The files in this package
contain font maps for dvipdfmx to make various
Japanese/Chinese/Korean fonts available for (u)ptex and related
programs and formats.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/ptex-fontmaps
%{_texmfdistdir}/texmf-dist/scripts/ptex-fontmaps
%{_texmfdistdir}/texmf-dist/fonts/misc/ptex-fontmaps
%{_texmfdistdir}/texmf-dist/fonts/map/dvipdfmx/ptex-fontmaps
%{_texmfdistdir}/texmf-dist/fonts/cmap/ptex-fontmaps
%doc %{_texmfdistdir}/texmf-dist/doc/fonts/ptex-fontmaps

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
