%global tl_name ptex-fontmaps
%global tl_revision 65953
%global tl_bin_links kanji-config-updmap:%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap.pl kanji-config-updmap-sys:%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap-sys.sh kanji-config-updmap-user:%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-config-updmap-user.sh kanji-fontmap-creator:%{_texmfdistdir}/scripts/ptex-fontmaps/kanji-fontmap-creator.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20210625.0
Release:	%{tl_revision}.1
Summary:	Font maps and configuration tools for Japanese/Chinese/Korean fonts with (u)ptex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ptex-fontmaps
License:	pd gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fontmaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fontmaps.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fontmaps.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ptex-fontmaps.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This package provides font maps and setup tools for Japanese, Korean,
Traditional Chinese, and Simplified Chinese. It is the successor of the
jfontmaps package. The files in this package contain font maps for
dvipdfmx to make various Japanese/Chinese/Korean fonts available for
(u)ptex and related programs and formats.

