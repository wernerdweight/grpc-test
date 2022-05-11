<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ovm.proto

namespace Ovm;

use UnexpectedValueException;

/**
 * Protobuf type <code>ovm.Mood</code>
 */
class Mood
{
    /**
     * Generated from protobuf enum <code>GOOD = 0;</code>
     */
    const GOOD = 0;
    /**
     * Generated from protobuf enum <code>NOT_GREAT_NOT_TERRIBLE = 2;</code>
     */
    const NOT_GREAT_NOT_TERRIBLE = 2;
    /**
     * Generated from protobuf enum <code>BAD = 3;</code>
     */
    const BAD = 3;
    /**
     * Generated from protobuf enum <code>NOT_THIS_SHIT_AGAIN = 4;</code>
     */
    const NOT_THIS_SHIT_AGAIN = 4;

    private static $valueToName = [
        self::GOOD => 'GOOD',
        self::NOT_GREAT_NOT_TERRIBLE => 'NOT_GREAT_NOT_TERRIBLE',
        self::BAD => 'BAD',
        self::NOT_THIS_SHIT_AGAIN => 'NOT_THIS_SHIT_AGAIN',
    ];

    public static function name($value)
    {
        if (!isset(self::$valueToName[$value])) {
            throw new UnexpectedValueException(sprintf(
                    'Enum %s has no name defined for value %s', __CLASS__, $value));
        }
        return self::$valueToName[$value];
    }


    public static function value($name)
    {
        $const = __CLASS__ . '::' . strtoupper($name);
        if (!defined($const)) {
            throw new UnexpectedValueException(sprintf(
                    'Enum %s has no value defined for name %s', __CLASS__, $name));
        }
        return constant($const);
    }
}
