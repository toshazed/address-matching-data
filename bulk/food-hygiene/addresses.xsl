<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text" encoding="UTF-8"/>

<xsl:template match="/">
  <xsl:apply-templates select="//EstablishmentDetail"/>
</xsl:template>

<!-- text	name	business	premises	local-authority	food-premises-types -->

<xsl:template match="EstablishmentDetail">
<xsl:if test="AddressLine1">
  <!-- test -->FHRS:<xsl:value-of select="FHRSID"/><xsl:text>&#9;</xsl:text>
  <!-- name --><xsl:value-of select="BusinessName"/><xsl:text>&#9;</xsl:text>
  <!-- address text --><xsl:value-of select="AddressLine1"/><xsl:text>, </xsl:text>
  <!-- address text --><xsl:value-of select="AddressLine2"/><xsl:text>, </xsl:text>
  <!-- address text --><xsl:value-of select="AddressLine3"/><xsl:text>, </xsl:text>
  <!-- address text --><xsl:value-of select="AddressLine4"/><xsl:text>&#9;</xsl:text>
  <!-- postcode --><xsl:value-of select="PostCode"/><xsl:text>&#9;</xsl:text>
  <!-- food-authority --><xsl:value-of select="LocalAuthorityCode"/><xsl:text>&#9;</xsl:text>
<xsl:if test="Geocode/Latitude">
  <!-- latitude --><xsl:text>[</xsl:text><xsl:value-of select="format-number(Geocode/Latitude, '#0.00000')" /><xsl:text>,</xsl:text>
  <!-- longitude --><xsl:value-of select="format-number(Geocode/Longitude, '#0.00000')" /><xsl:text>]</xsl:text>
</xsl:if><xsl:text>
</xsl:text>
</xsl:if>
</xsl:template>

</xsl:stylesheet>
